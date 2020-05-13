<?php
   function run($name) {
      $data = ini_get($name);
      return array_filter(preg_split('/\s*,\s*/', $data));
   }
   echo json_encode(array (
      'disable_functions' => run('disable_functions'), 
      'disable_classes'   => run('disable_classes')
   ));
?>

