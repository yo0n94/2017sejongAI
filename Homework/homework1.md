# Sentiment Analyzer


## 가설 1: 5줄 이상의 긴 리뷰가 2-3줄의 짧은 리뷰보다 결과 점수가 높을 것이다.

### 가설 설정 이유 : 문장이 길수록 단어가 많이 포함되므로 점수를 평가할 때 더 많은 영향을 미쳐 높은 점수가 나올 것이라고 예상했다.

**검증 방법** : 점수가 높은 긴 리뷰들 중 중요한 문장, 긍정과 부정의 의미를 전달한다고 생각한 문장으로 추려 테스트 해보았다.

[Used code](https://github.cgithub.com/yo0n94/2017sejongAI/blob/master/Homework/%EA%B0%80%EC%84%A41%20%EA%B8%B4%EB%AC%B8%EC%9E%A5%EC%A7%A7%EC%9D%80%EB%AC%B8%EC%9E%A5%EC%B0%A8%EC%9D%B4.py)

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

-> **결론** 
**부정일 때는 리뷰의 길이에 거의 영향을 받지 않았는데, 긍정일 때는 글이 짧아질수록 영향을 받아 점수가 낮아졌다.**

----------------------------------------------------------------


## 가설 2: 느낌표(!)를 붙이면 점수가 높아질 것이다. 

### 가설 설정 이유 : 느낌표는 문장 끝에서 문장 전체를 강조하는 역할을 하기 때문에 점수를 높게 할 것이라 예상했다.

**검증 방법** : 똑같은 리뷰 중 강조해야겠다고 느낀 문장 끝에 느낌표를 붙여 비교해본다.

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

-> **결론** 
**긍정과 부정 리뷰 모두 느낌표를 붙였을 때, 같은 내용이어도 느낌표의 영향을 받아 점수가 더 높아졌다.**

----------------------------------------------------------------
