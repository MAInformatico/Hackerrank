data=($(cat))
echo ${data[@]/*[aA]*/}
