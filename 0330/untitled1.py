# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 14:36:35 2022

@author: Thinkpad
08z"""

def display_board(b):
    "显示棋盘"
    print("\t{0}|{1}|{2}".format(b[0],b[1],b[2]))
    print("\t_|_|_")
    print("\t{0}|{1}|{2}".format(b[3],b[4],b[5]))
    print("\t_|_|_")
    print("\t{0}|{1}|{2}".format(b[6],b[7],b[8]))
    
def legal_moves(board):
    #返回可落子位置列表
    moves=[]
    for i in range(9):
        if board[i] in list("012345678"):
            moves.append(i)
    return moves

def getPlayerMove(board):
    #询问并确认玩家的落子位置，无效位置重复询问
    move=9
    while move not in legal_moves(board):
        move = int(input("请选择落子位子（0-8）:"))
    return move

def getComputerMove(board,computerLetter,playerLetter):
    #计算人工智能的落子位置
    boardcopy=board.copy()
    #规则1,如果落子在某处能获胜，则落在该位置
    for move in legal_moves(boardcopy):
        boardcopy[move]=computerLetter
        if isWinner(boardcopy,computerLetter):
            return move
        boardcopy[move]=str(move)
        
    #规则2:某位置玩家下一步可获胜，选择该位置
    for move in legal_moves(boardcopy):
        boardcopy[move]=playerLetter
        if isWinner(boardcopy,playerLetter):
            return move
        boardcopy[move]=str(move)
        
    #规则3：按照中心（4）、角（0，2，6，8）、边（1，3，5，7）的顺序选择位置
    for move in(4,0,2,6,8,1,3,5,7):
        if move in legal_moves(board):
            return move
        
def isWinner(board,letter):
    #判断给的棋子是否获胜
    WAYS_TO_WIN={(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)}
    for r in WAYS_TO_WIN:
        if board[r[0]]==board[r[1]]==board[r[2]]:
            return True
    return False

def isTie(board):
    #是否平局
    for i in list("012345678"):
        if i in board:
            return False
    return True

def tic_tac_toe():
    #井字棋
    #初始化棋盘为【‘0’，‘1’，‘2’，‘3’，‘4’，‘5’，‘6’，‘7’，‘8’】
    board=list("012345678")
    #询问玩家选择棋子
    playerLetter=input("请选择棋子X或O(X先走，O后走):")
    if playerLetter in("X","x"):
        turn="player"
        computerLetter="O"
    else:
        turn="computer"
        computerLetter="X"
        playerLetter="O"
        print("{}先走".format(turn))
    
    while True:#轮流落子
        display_board(board)
        if turn=='player':
            move=getPlayerMove(board) #询问落子位置
            board[move]=playerLetter #落子
            if isWinner(board,playerLetter): #判断是否获胜
                display_board(board)
                print("恭喜玩家获胜!")
                break
            else:
                turn='computer'
        else:
            #计算人工智能落子位置
            move=getComputerMove(board,computerLetter,playerLetter)
            print("计算机人工智能AI落子位置：",move)
            board[move]=computerLetter #落子
            if isWinner(board,computerLetter): #判断是否获胜
                display_board(board)
                print("计算机人工智能AI获胜！")
                break
            else:
                turn='player'
                
        #判断是否平局
        if isTie(board):
            display_board(board)
            print("平局！")
            break
        
tic_tac_toe()
        
   