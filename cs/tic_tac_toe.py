# 模块：c:/pythonpa/cs/tic_tac_toe.py  
def display_board(b):
    """显示棋盘"""
    print("\t{0}|{1}|{2}".format(b[0],b[1],b[2]))
    print("\t_|_|_")
    print("\t{0}|{1}|{2}".format(b[3],b[4],b[5]))
    print("\t_|_|_")
    print("\t{0}|{1}|{2}".format(b[6],b[7],b[8]))

def legal_moves(board):
    """返回可落子的位置列表"""
    moves = []
    for i in range(9):
        if board[i] in list("012345678"):
            moves.append(i)
    return moves

def getPlayerMove(board):  
    """询问并确定玩家(player)选择落子位置，无效位置时重复询问"""
    move = 9 # 初始值9为错误的位置
    while move not in legal_moves(board):  
        move = int(input("请选择落子位置(0-8):"))
    return move

def getComputerMove(board, computerLetter, playerLetter):         
    """计算人工智能AI的落子位置, Tic Tac Toe AI核心算法"""  
    boardcopy = board.copy() #拷贝棋盘，不影响原来
    # 规则1：判断如果某位置落子可获胜，则选择该位置  
    for move in legal_moves(boardcopy):
        boardcopy[move] = computerLetter
        if isWinner(boardcopy, computerLetter): #判断是否获胜 
            return move
        boardcopy[move] = str(move)
            
    # 规则2：某个位置玩家下一步落子可获胜，则选择该位置  
    for move in legal_moves(boardcopy):
        boardcopy[move] = playerLetter
        if isWinner(boardcopy, playerLetter): #判断是否获胜 
            return move     
        boardcopy[move] = str(move)
    # 规则2：中心（4）、角（0、2、6、8）、边（1、3、5、7）顺序选择空的位置
    for move in (4,0,2,6,8,1,3,5,7):
        if move in legal_moves(board):
            return move

def isWinner(board, letter): 
    """判断所给的棋子是否获胜"""
    WAYS_TO_WIN = {(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),
    (0,4,8), (2,4,6)}
    for r in WAYS_TO_WIN:
        if board[r[0]]==board[r[1]]==board[r[2]]:
            return True
    return False

def isTie(board):
    """判断是否平局"""
    for i in list("012345678"):
        if i in board:
            return False
    return True

def tic_tac_toe():
    """井字棋"""
    #初始化棋盘为['0', '1', '2', '3', '4', '5', '6', '7', '8']
    board = list("012345678")
    #询问玩家选择棋子：棋子X先走，棋子O后走
    playerLetter = input("请选择棋子X或O（X先走，O后走）：")
    if playerLetter in ("X", "x"):
        turn = "player"   #玩家先走
        computerLetter = "O"
    else:
        turn = "computer"
        computerLetter = "X"
        playerLetter = "O"
    print("{}先走!".format(turn)) 

    while True: #循环轮流落子
        display_board(board)  
        if turn == 'player':  # 玩家落子          
            move = getPlayerMove(board) #询问落子位置
            board[move] = playerLetter  #落子
            if isWinner(board, playerLetter): #判断是否获胜  
                display_board(board)   
                print('恭喜玩家获胜!')  
                break
            else:
                turn = "computer"
        else:  #计算机人工智能AI落子
            # 计算人工智能计算AI落子位置
            move = getComputerMove(board, computerLetter, playerLetter) 
            print("计算机人工智能AI落子位置：", move)
            board[move] = computerLetter  #落子
            if isWinner(board, computerLetter): #判断是否获胜  
                display_board(board)   
                print('计算机人工智能AI获胜!')  
                break
            else:
                turn = "player"       
        #判断是否平局 
        if isTie(board):  
            display_board(board)   
            print('平局!')  
            break
    
if __name__ == '__main__':
    tic_tac_toe()