for dir in ./test_inputs/*/     # list directories in the form "/tmp/dirname/"
do    
    #echo `basename $dir`  # print everything after the final "/"
    var="${dir}parameters.json"
    echo "=============${var}==============="
    `python rad_main.py -p ${var}`
done
