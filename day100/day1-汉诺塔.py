'''
将 N 个圆盘从左边柱子移动到右边柱子：

[递归的]将 N-1 个圆盘从左边柱子移动到中间柱子。
将最大的圆盘从左边柱子移动到右边柱子。
[递归的]将 N-1 个圆盘从中间柱子移动到右边柱子。
'''
def hano(height, left='left', right='right', midle='midle'):
    if height:
        hano(height-1,left,midle,right)
        print(height,left ,"->", right)
        hano(height-1,midle,right,left)

hano(3)
        
    
