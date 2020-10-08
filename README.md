<h1>EX1  面積與周長</h1>
<h2>輸入直徑，計算出面積與周長，並輸出至小數點以下兩位

Hint: 
可用math.pi

測試資料:
</h2>
<table>
<th>輸入</th><th>輸出</th>
<tr>
  <td>2</td><td>3.14, 6.28</td>
</tr>
<tr>
  <td>10</td><td>78.54, 31.42</td>
</table>

<h1>EX2  計算距離</h1>
<h2>輸入兩個座標，輸出距離。
透過input詢問四次，取得兩個點x, y座標，透過平面距離公式計算出兩點距離(取到小數點以下二位)。
輸出時，請用print(“”.format())印出以下效果:

(1, 1)到(9, 8)的距離為10.63

Hint: 開根號可用math.sqrt()

測試資料:
</h2>
<table>
<th>輸入</th><th>輸出</th>
<tr>
  <td>(1, 1), (1, 2)</td><td>1</td>
</tr>
<tr>
  <td>(1, 1), (9, 8)</td><td>10.63</td>
</table>

<h1>EX3  str.split()</h1>
<h2>同上一題，但一次輸入一個座標(例: 11,2)，你的程式必須解析把它分成11與2兩個字串，再轉成整數
</h2>

<h1>EX4   標準差</h1>
<h2>學生的成績為: 10, 30, 40, 90, 100, 62

1. 計算其平均:
	a. 四捨五入
	b. 無條件進位
	c. 無條件捨去
2. 計算成績標準差
</h2>
<table>
<th>輸入</th><th>輸出</th>
<tr>
  <td>1</td><td></td>
</tr>
<tr>
  <td>1a</td><td>55</td>
</tr>
<tr>
  <td>1b</td><td>56</td>
</tr>
<tr>
  <td>1c</td><td>55</td>
</tr>
<tr>
  <td>2</td><td>32.08</td>
</tr>
</table>

<h1>EX5  Guess Number Game</h1>
<h2>
請將範例程式碼demo_guessnumber.py修正成能夠持續輸入至猜中數字為止。
</h2>
<h3>
import random<br>
cmp = random.randint(1, 100)<br>
<br>
guess = input("Guess a number between 1 and 100: ")<br>
<br>
while not guess.isdigit():<br>
    guess = input("Wrong input, Please input a number: ")<br>
<br>
guess = int(guess)<br>
while guess > 100 or guess < 1:<br>
    guess = input("The number must between 1-100: ")<br>
<br>
if(cmp == guess):<br>
    print("Correct!!")<br>
elif(cmp > guess):<br>
    print("Guess a large number")<br>
else: <br>
    print("Guess a small number")<br>
</h3>

<h1>EX6  中英字典</h1>
<h2>應用dict建立一個英翻中的字典，例如myDict = {“dog”: “狗”, “cat”:“貓” }。依據此字典透過程式產生另一個中翻英字典。

1.要求使用者選擇: 英翻中, 中翻英,或離開<br>
2.使用者輸入英文(或中文)<br>
3.若有此字，輸出翻譯結果，若沒有，則輸出:查無此單字。<br>
4.迴圈直到使用者選擇離開<br>

</h2>
<a href="https://imgur.com/SkiwHVE"><img src="https://i.imgur.com/SkiwHVE.png" title="source: imgur.com" /></a>

<h1>EX7 最大和</h1>
<h2>
<span><strong>問題描述</strong></span><br>
    給定 N 群數字，每群都恰有 M 個正整數。若從每群數字中各選擇一個數字 (假設第 i 群所選出數字為 ti )，將所選出的 N 個數字加總即可得總和 S = t1+t2+…+tN。請寫程式計算 S 的最大值 (最大總和)，並判斷各群所選出的數字是否可以整除 S。<br>
<br>
<span><strong>輸入格式</strong></span><br>
    第一行有二個正整數 N 和 M， 1≦ N ≦ 20，1≦ M ≦ 20。 接下來的 N 行，每一行各有 M 個正整數 xi ，代表一群整數，數字與數字間有一個空 格，且 1≦ i ≦M，以及 1≦ xi ≦256。<br>
<br>
<span><strong>輸出格式</strong></span><br>
    第一行輸出最大總和 S。 第二行按照被選擇數字所屬群的順序，輸出可以整除 S 的被選擇數字，數字與數字間 以一個空格隔開，最後一個數字後無空白；若 N 個被選擇數字都不能整除 S，就輸出-1。<br>
</strong>
</h2>
<a href="https://imgur.com/m5MNZgV"><img src="https://i.imgur.com/m5MNZgV.png" title="source: imgur.com" /></a>
