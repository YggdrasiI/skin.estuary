# Add scale params to tags like
# <param name="width|height|etc" value="number">
s/<param name="\(left\|right\|width\|posx\|left_posx\|right_posx\)" value="\([-]\{0,1\}[0-9]\+\)"/<param name="\1" value="{{ScaleX('\2')}}"/g
s/<param name="\(top\|bottom\|height\|posy\|down_posy\|up_posy\)" value="\([-]\{0,1\}[0-9]\+\)"/<param name="\1" value="{{ScaleY('\2')}}"/g

