<?php
$handle = fopen ("php://stdin","r");

    function fibonacci($n) {
        if ($n == 0) 
            return 0;     
        else if ($n == 1) 
            return 1;     
        
        else
            return (Fibonacci($n-1) +  Fibonacci($n-2));         
    }

    $n = fgets($handle);

    printf("%d", fibonacci($n));

fclose($handle);
?>
