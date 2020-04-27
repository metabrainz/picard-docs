<!DOCTYPE html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Language Redirect Testing</title>
</head>
<?php
#################################################################################
#   Copyright © 2008 Darrin Yeager                                              #
#   https://www.dyeager.org/                                                    #
#   Licensed under BSD license.                                                 #
#   https://www.dyeager.org/downloads/license-bsd.txt                           #
#   https://www.dyeager.org/2008/10/getting-browser-default-language-php.html   #
#################################################################################

function getDefaultLanguage() {
   if (isset($_SERVER["HTTP_ACCEPT_LANGUAGE"]))
      return parseDefaultLanguage($_SERVER["HTTP_ACCEPT_LANGUAGE"]);
   else
      return parseDefaultLanguage(NULL);
   }

function parseDefaultLanguage($http_accept, $deflang = "en") {
   if(isset($http_accept) && strlen($http_accept) > 1)  {
      # Split possible languages into array
      $x = explode(",",$http_accept);
      foreach ($x as $val) {
         #check for q-value and create associative array. No q-value means 1 by rule
         if(preg_match("/(.*);q=([0-1]{0,1}.\d{0,4})/i",$val,$matches))
            $lang[$matches[1]] = (float)$matches[2];
         else
            $lang[$val] = 1.0;
      }

      #return default language (highest q-value)
      $qval = 0.0;
      foreach ($lang as $key => $value) {
         if ($value > $qval) {
            $qval = (float)$value;
            $key = substr($key, 0, 2);
            if (strpos("en es fr de", $key) !== false) {
               $deflang = $key;
            }
         }
      }
   }
   return strtolower($deflang);
}

$junk = isset($_SERVER["HTTP_ACCEPT_LANGUAGE"]) ? $_SERVER["HTTP_ACCEPT_LANGUAGE"] : 'none';
// echo "<p>HTTP_ACCEPT_LANGUAGE = '" . $junk . "'</p>\n";
// echo "<p>Preferred Language = '" . getDefaultLanguage() . "'</p>\n";
?>
<body onload="window.location.replace('/<?php echo getDefaultLanguage(); ?>/html/index.html');">
</body>
</html>