# Sentiment Analyzer


## 가설 1: 5줄 이상의 긴 리뷰가 2-3줄의 짧은 리뷰보다 결과 점수가 높을 것이다.

### 가설 설정 이유 : 문장이 길수록 단어가 많이 포함되므로 점수를 평가할 때 더 많은 영향을 미쳐 높은 점수가 나올 것이라고 예상했다.

**-검증 방법** : 점수가 높은 긴 리뷰들 중 중요한 문장, 긍정과 부정의 의미를 전달한다고 생각한 문장으로 추려 테스트 해보았다.

[Used code](https://github.com/yo0n94/2017sejongAI/blob/master/Homework/%EA%B0%80%EC%84%A41%20%EA%B8%B4%EB%AC%B8%EC%9E%A5%EC%A7%A7%EC%9D%80%EB%AC%B8%EC%9E%A5%EC%B0%A8%EC%9D%B4.py)

Review: I loved that movie for all what was
said before I do, but I see one additional plus: maybe the genius side of the
writer and the Director: You can see the movie two ways: 1 - Like the probable
intention of the author: a couple, on the breaking point, because he is too
busy to love freely; an accident, she dies. He is drowning in his grief, and
his conscience makes him re-live the story where he realizes his shortcomings,
his losses, and punishing himself, he dies at the end. 2 - The movie start on
what we can around the middle believe it's a dream (premonition?). When he
wakes up, relieved, he understood the message of his dream 'love fully, for 5
minutes or 50 years, but fully'. He apply this lesson, 'as if it is his last
day', touches the happiness of love, and, in a twist of the fate, dies in the
accident he was dreaming, the night before that his love lost her life. No
matter the way you watch this movie, it's a piece of Art; the makers are
geniuses How about an award? would it not deserve one?

Predicted sentiment: Positive
Probability: 1.0


Review: I DO NOT WANT TO WRITE 10 LINES.
JUST want to tell u all who haven't seen it yet that its really PERFECT. Maybe
my best movie ever. all rest lines from now on are just for get the minimum 10
lines. no actually need to read if you do not want. The passion. the love. the
feelings this movie emit are all so ...HUGE. I feel so happy than even after 10
years of movies creation i found it. i had no idea this film even exist. i feel
that for some maybe this movie will be even life changer. both actors were v
good . all were marvelous. songs. landscapes. everything. masterpiece !! ending
? one of best ever seen. so simple but same time so great. take your wife /
husband .. hug him/her and stay this way till the end of film. without kids,
just u 2.

Predicted sentiment: Positive
Probability: 0.99

 
Review: This movie fails on every level. I
can't recall ever seeing such trivial drivel pathetically attempting to
masquerade as a meaningful story. The plot? There wasn't one. The characters?
Stupid and shallow. Good points? That it finally ended. Why I watched it to the
end? The hope that beats eternal. Don't waste your money, not even as a weekly
video for two bucks. If it comes on free-to-air, bypass it. The last movie I
recall that was as bad as this was Kramer versus Kramer. This was an attempt to
take a teenybopper B grade comic-book love story and turn it into a meaningful
movie. For whom? Pre-pubescent fairytalers probably, and I imagine it even
failed for them. 

Predicted sentiment: Negative
Probability: 1.0

 
Review: This is one of the very worst
movies I have ever rented.... the acting was terrible, apart from the taxi
driver played by Tom Williamson.. what was he doing in a movie as poor as this?
Paul Nicholas (who looks a little like Jude Law, but in this case thats as far
as it goes..) has the most terrible Northern English accent I have heard. I
have not seen or heard of this actor before, but would not go out of my way to
see him again, I could have played the part better and I am a five foot 2
female. Jennifer Love Hewitt was perfectly sickly, I am sure I have seen her do
better than this. Apart from the awful acting, the storyline was just way too
cheesy and it took forever to end, the twist at the end didn't work... it came
an hour too late (real time...). 

Predicted sentiment: Negative
Probability: 0.99


Review: I loved that movie for all what was
said before I do, but I see one additional plus: maybe the genius side of the
writer and the Director. No matter the way you watch this movie, it's a piece
of Art; the makers are geniuses How about an award? would it not deserve one?

Predicted sentiment: Positive
Probability: 0.75


Review: I JUST want to tell u all who
haven't seen it yet that its really PERFECT. Maybe my best movie ever. The
passion. the love. the feelings this movie emit are all so ...HUGE. I feel so
happy than even after 10 years of movies creation.

Predicted sentiment: Positive
Probability: 0.84


Review: This movie fails on every level. I
can't recall ever seeing such trivial drivel pathetically attempting to
masquerade as a meaningful story. The plot? There wasn't one. The characters?
Stupid and shallow.

Predicted sentiment: Negative
Probability: 0.99

 
Review: This is one of the very worst
movies I have ever rented.... the acting was terrible. The most terrible
Northern English accent I have heard. Apart from the awful acting, the
storyline was just way too cheesy and it took forever to end.

Predicted sentiment: Negative
Probability: 0.99

>결론
**부정일 때는 리뷰의 길이에 거의 영향을 받지 않았는데, 긍정일 때는 글이 짧아질수록 영향을 받아 점수가 낮아졌다.**

----------------------------------------------------------------


## 가설 2: 느낌표(!)를 붙이면 점수가 높아질 것이다. 

### 가설 설정 이유 : 느낌표는 문장 끝에서 문장 전체를 강조하는 역할을 하기 때문에 점수를 높게 할 것이라 예상했다.

**-검증 방법** : 똑같은 리뷰 중 강조해야겠다고 느낀 문장 끝에 느낌표를 붙여 비교해본다.

[Used code](https://github.com/yo0n94/2017sejongAI/blob/master/Homework/%EA%B0%80%EC%84%A42%20%EB%8A%90%EB%82%8C%ED%91%9C.py)

Review: About Time was one of the greatest
movies I have ever seen. I was immediately captured, and the cast is so
brilliant, I believed every single line. Thank you for this film, I am still
under the influence of this movie. 

Predicted sentiment: Positive
Probability: 0.9


Review: About Time was one of the greatest
movies I have ever seen !!!! I was immediately captured, and the cast is so
brilliant, I believed every single line. Thank you for this film !! I am still
under the influence of this movie.

Predicted sentiment: Positive
Probability: 0.92

 
Review: Without doubt one of the worst
films I have ever seen. Storyline - banal bordering on silly. Every character
totally miscast. 

Predicted sentiment: Negative
Probability: 0.88


Review: Without doubt one of the worst
films I have ever seen. Storyline - banal bordering on silly. Every character
totally miscast !!!!!! 

Predicted sentiment: Negative
Probability: 0.96

>결론 
**긍정과 부정 리뷰 모두 느낌표를 붙였을 때, 같은 내용이어도 느낌표의 영향을 받아 점수가 더 높아졌다.**

----------------------------------------------------------------

## 가설 3: 문장 끝에 …을 붙이면 점수에 영향을 끼칠 것이다.

### 가설 설정 이유 : …은 보통 말을 잇지 못하거나 생략할 때 쓰므로 영향을 받을 것이라고 예상했다.

**-검증 방법** : 같은 리뷰의 문장 끝에 …을 붙여 비교한다. + !!!도 붙여서 비교해본다.

[Used code]( https://github.com/yo0n94/2017sejongAI/blob/master/Homework/%EA%B0%80%EC%84%A43%20%EC%9D%BC%EB%B0%98%2C%2C%2C!!!.py)

Review: Majority of the critics are fake
here and that’s the only reason for such a high rating for this dumb movie. Don't watch.
Total waste. Wish I could time travel and bring those valuable time back.

Predicted sentiment: Negative
Probability: 0.86


Review: Majority of the critics are fake
here and that’s the only reason for such a high rating for this dumb
movie...... Don't watch….. Total waste.... Wish I could time travel and bring
those valuable time back…….

Predicted sentiment: Negative
Probability: 0.86


Review: Majority of the critics are fake
here and that’s the only reason for such a high rating for this dumb movie !
Don't watch ! Total waste ! Wish I could time travel and bring those valuable
time back !

Predicted sentiment: Negative
Probability: 0.98
 

Review: Now here's the romance of the
decade. Heart-warming doesn't even come close to describing 'If Only' It's a
story about love in it's purest form. About realizing that any moment some one
you care for can be taken away and you have the be certain you did everything
to make your life meaningful with that some one. If you're looking for a movie
that will make you smile, make you think, make you cry and leave you touched.
If Only is the way to go.

Predicted sentiment: Positive
Probability: 0.85


Review: Now here's the romance of the
decade..... Heart-warming doesn't even come close to describing 'If Only' It's
a story about love in it's purest form..... About realizing that any moment
some one you care for can be taken away and you have the be certain you did
everything to make your life meaningful with that some one.... If you're
looking for a movie that will make you smile, make you think, make you cry and
leave you touched...... If Only is the way to go.....

Predicted sentiment: Positive
Probability: 0.85


Review: Now here's the romance of the
decade! Heart-warming doesn't even come close to describing 'If Only' It's a
story about love in it's purest form ! About realizing that any moment some one
you care for can be taken away and you have the be certain you did everything
to make your life meaningful with that some one! If you're looking for a movie
that will make you smile, make you think, make you cry and leave you touched !
If Only is the way to go!

Predicted sentiment: Positive
Probability: 0.94

>결론 
**...은 어디에도 영향을 미치지 않았다. 하지만 느낌표는 영향을 받아 점수가 더 높아졌다.**
----------------------------------------------------------------

## 가설 4: 감탄사, 약어, 비속어를 인식하고 점수에 영향을 미칠 것이다.

### 가설 설정 이유 : 영어에서 널리 쓰이는 감탄사, 약어, 비속어는 단어로 인식을 하고 형태에따라 긍정, 부정에 영향을 줄 것이라고 예상했다.

**-검증 방법** : 문장 사이 적절한 위치에 감탄사, 약어, 비속어를 넣고 들어가지 않았을 때와 비교한다.

[Used code](https://github.com/yo0n94/2017sejongAI/blob/master/Homework/%EA%B0%80%EC%84%A44%20%EC%95%BD%EC%96%B4%2C%EA%B0%90%ED%83%84%EC%82%AC%2C%EB%B9%84%EC%86%8D%EC%96%B4%20%EB%93%B1.py)

Review: 'WTF!' this movie was so
unbelievable and stupid. OMG Unromantic, boring, terribly acted... The list
goes on and on. Although I can't fault the blame totally on Love. LOL, None of
the actors were convincing at all, except maybe Tom Wilkenson, although I do 
think slightly less of him for taking part in this Damn horrible film. Yuck!

Predicted sentiment: Negative
Probability: 0.61 


Review: WOW!! Now here's the romance of the
decade. Heart-warming doesn't even come close to describing 'If Only' It's a
story about love in its purest form. OH, about realizing that any moment someone
you care for can be taken away and you have the be certain you did everything
to make your life meaningful with that someone. If you're looking for a movie
that will make you smile, make you think, make you cry and leave you touched.
If Only is the way to go. Hooray!
 
Predicted sentiment: Positive
Probability: 0.84


Review: This movie was so unbelievable and
stupid. Unromantic, boring, terribly acted... The list goes on and on. Although
I can't fault the blame totally on Love. None of the actors were convincing at
all, except maybe Tom Wilkenson, although I do think slightly less of him for
taking part in this horrible film.

Predicted sentiment: Negative
Probability: 0.61


Review: Now here's the romance of the
decade. Heart-warming doesn't even come close to describing 'If Only' It's a
story about love in its purest form. About realizing that any moment someone
you care for can be taken away and you have the be certain you did everything
to make your life meaningful with that someone. If you're looking for a movie
that will make you smile, make you think, make you cry and leave you touched.
If Only is the way to go.

Predicted sentiment: Positive
Probability: 0.84 

>결론 
**약어,감탄사,비속어를 인식하지 못하고 어디에도 영향을 미치지 않았다.**
----------------------------------------------------------------------

## 가설 5: 특정 단어를 대문자로 강조했을 때 점수에 영향을 미칠 것이다.

### 가설 설정 이유 : 한국어에는 없지만 영어에서는 대문자로 단어의 의미를 강조하기 때문에 이것을 인식할 것이라고 예상했다. 

**검증 방법** : 문장 내 긍정, 부정을 나타내는 특정 단어를 선택해 대문자로 강조하고 그렇지 않았을 때와 비교한다.

[Used code](https://github.com/yo0n94/2017sejongAI/blob/master/Homework/%EA%B0%80%EC%84%A45%20%EB%8C%80%EB%AC%B8%EC%9E%90%EA%B0%95%EC%A1%B0.py)

Review: The Notebook is the best movie I
have seen in a very long time! I love the story, the actors, the scenery...everything.
I have NEVER cried when I watched a movie and this one made me cry like a baby
in the theater. Which was very embarrassing if you ask me. But anyway, The
Notebook is the most touching love story I have ever seen.

Predicted sentiment: Positive
Probability: 0.82


Review: The Notebook is the BEST movie I
have seen in a very long time! I LOVE the story, the actors, the
scenery...everything. I have never cried when I watched a movie and this one
made me cry like a baby in the theater. Which was very embarrassing if you ask
me. But anyway, The Notebook is the MOST TOUCHING LOVE STORY I have ever seen.

Predicted sentiment: Negative
Probability: 0.54


Review: The characters are dull! Noah is
what? Manic-depressive? Manic in the first 5 minutes, and throughout the rest
of the movie depressive. The music is simply unbearable! And sooooooo many
other bugs... Damn I don't even know why I'm writing this. I feel like one of
Jeffrey Dahmer's zombies. Even that should feel better than being this numb
after watching this piece of... you know what.!!

Predicted sentiment: Negative
Probability: 0.73


Review: The characters are DULL! Noah is
what? MANIC-DEPRESSIVE? Manic in the first 5 minutes, and throughout the rest
of the movie depressive. The music is simply UNBEARABLE! And sooooo many other
BUGS... Damn I don't even know why I'm writing this. I feel like one of Jeffrey
Dahmer's zombies. Even that should feel better than being this numb after
watching this piece of... you know what.!!

Predicted sentiment: Positive
Probability: 0.53


Review: Now here's the romance of the
decade. Heart-warming doesn't even come close to describing 'If Only' It's a
story about love in it's purest form. About realizing that any moment some one
you care for can be taken away and you have the be certain you did everything
to make your life meaningful with that some one. If you're looking for a movie
that will make you smile, make you think, make you cry and leave you touched.
If Only is the way to go.

Predicted sentiment: Positive
Probability: 0.84


Review: Now here's the ROMANCE of the
decade. HEART-WARMING doesn't even come close to describing 'If Only' It's a
story about LOVE in it's PUREST form. About realizing that any moment some one
you care for can be taken away and you have the be certain you did everything
to make your life meaningful with that some one. If you're looking for a movie
that will make you SMILE, make you think, make you cry and leave you touched.
If Only is the way to go.

Predicted sentiment: Negative
Probability: 0.54

>결론 
**문장 내 특정 단어를 강조했을 때 긍정은 부정으로 부정은 긍정 리뷰로 바뀌었다. 강조가 여러 번 돼서 반대의 영향을 끼치지 않았나..**
----------------------------------------------------------------------
