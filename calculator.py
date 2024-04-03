class Calculator:
    """四則演算を行うクラス."""

    # 足し算を行う関数を実装してください
    @staticmethod
    def add(a, b)-> int:
        #     """足し算を行う."""
        return a + b

    # 引き算を行う関数を実装してください
    @staticmethod
    def sub(a, b)-> int:
        #     """引き算を行う."""
        return a - b
    
    # 掛け算を行う関数を実装してください
    @staticmethod
    def mul(a, b) -> int:
        #     """掛け算を行う."""
        return a * b
    # 割り算を行う関数を実装してください
    @staticmethod
    def dev(a, b) -> float:
        #     """割り算を行う."""
        return a / b
    # 文字列を入力すると計算結果を返す関数を実装してください
    # @staticmethod
    # def cal_formula(formula:str) -> float:
    #     """計算式の分割と計算"""


# テストコード
if __name__ == '__main__':
    numa = 22
    numb = 11

    # 各関数のテストコードを作成してください
    #足し算
    print("addition > ", Calculator.add(numa, numb))
    #引き算
    print("substraction > ", Calculator.sub(numa, numb))
    #掛け算
    print("multiplication > ", Calculator.mul(numa, numb))
    #割り算
    print("division > ", Calculator.div(numa, numb))
    # 文字列の読み込み
    

    # 計算

    # 結果の表示
