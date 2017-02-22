/<animation [^$>]*effect="zoom"/ {
  s/center="\([^$"]*\)"/center="{{ScaleBorder2('\1')}}"/ 
}

