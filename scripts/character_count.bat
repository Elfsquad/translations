@ECHO OFF
SET "inputFile=.\ems_translations.csv"
powershell -NoLogo -NoProfile -Command ^
    "$counter = 0;" ^
    "Get-Content -Path '%inputFile%' |" ^
        "ForEach-Object {" ^
            "$counter++;" ^
            "$ns = $_ -replace ';','';" ^
            "if (($_.Length - $ns.Length) -ne 11) {" ^
                "'Iteration {0}: Length is {1}' -f $counter, ($_.Length - $ns.Length)" ^
            "}" ^
        "}"