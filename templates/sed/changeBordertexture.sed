# $ to skip lines with $PARAM
s/<bordertexture border="\([^$<]\+\)"/<bordertexture border="{{ScaleX('\1')}}"/g
