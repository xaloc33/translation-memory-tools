<?php
if ($_FILES["file"]["error"] > 0)
  {
  echo "Error: " . $_FILES["file"]["error"] . "<br>";
  }
else
  {
#  echo "Upload: " . $_FILES["file"]["name"] . "<br>";
#  echo "Type: " . $_FILES["file"]["type"] . "<br>";
#  echo "Size: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
#  echo "Stored in: " . $_FILES["file"]["tmp_name"];
  }


$tempdir = sys_get_temp_dir ();
$location = $_FILES["file"]["tmp_name"];
$out_file = sys_get_temp_dir();
$out_file .=  "/tm-" . $_FILES["file"]["name"];

echo $out_file;

die("finished");

#$out_file .= ".po";

#echo "Pas 1 ";
#echo $out_file;
#echo "  ";
#echo $location;

#echo " Pas 2 ";

#echo "msgmerge -N "  . $location  . " " .   $location . " -C tm.po > output.po 2> /dev/null";

#$command = "cp " . $location . $out_file;

#echo $command;
#exec($command,  $output, $return_value);

#echo out . $output[0];
#echo ret . $return_value;

#$command = "msgmerge -N "  . $location  . " " . $location . " -C tm.po > " . $out_file  . " 2> /dev/null";

#$echo $command;
#$exec($command,  $output, $return_value);



#echo out . $output[0];
#echo ret . $return_value;

#$attachment_location = $out_file;
#if (file_exists($attachment_location)) {
#
 #   header($_SERVER["SERVER_PROTOCOL"] . " 200 OK");
 #   header("Cache-Control: public"); // needed for i.e.
 #   header("Content-Type: application/po");
#    header("Content-Transfer-Encoding: Binary");
#    header("Content-Length:".filesize($attachment_location));
#    header("Content-Disposition: attachment; filename=" . $out_file);
#    readfile($attachment_location);
#    die();        
#} else {
#	echo "File :" . $attachment_location;
#	die("Error: File not found. ");
#} 

?> 