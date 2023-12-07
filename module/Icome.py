class Icome:
    yunjae = 0
    suzuka = 0

    def set_icome():
        Icome.yunjae = int(input('ユンジェの収入を入力'))
        Icome.suzuka = int(input('涼加の収入を入力'))
    
    def get_icome():      
        return (str(Icome.yunjae),str(Icome.suzuka))
    
