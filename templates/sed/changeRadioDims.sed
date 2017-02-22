# $ to skip lines with $PARAM
s/<radiowidth>\([^$<]\+\)</<radiowidth>{{ScaleX('\1')}}</g
s/<radioheight>\([^$<]\+\)</<radioheight>{{ScaleY('\1')}}</g
