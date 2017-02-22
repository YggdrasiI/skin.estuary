# Add scale params to tags like
# <param name="width|height|etc">number<
s/<param name="\(left\|right\|width\|posx\|left_posx\|right_posx\|textoffsetx\)">\([-]\{0,1\}[0-9]\+\)</<param name="\1">{{ScaleX('\2')}}</g
s/<param name="\(top\|bottom\|height\|posy\|down_posy\|up_posy\|textoffsety\)">\([-]\{0,1\}[0-9]\+\)</<param name="\1">{{ScaleY('\2')}}</g

