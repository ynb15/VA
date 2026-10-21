# Scott Aaronson — Transkript in VEROEFFENTLICHTER Zeit

**Zeiten passen zur Datei `YNB Podcast Scott Aaronson.mp4` (94:58)**, nicht zum
Rohton. Umgerechnet am 21.10.2026 mit dem gemessenen Modell:

| | |
|---|---|
| Tempo | **1,0999** (Ausgleichsgerade ueber 16 Fundstellen) |
| Vorlauf abgeschnitten | **13,2 s** (gefittet; Lautstaerkemessung sagt 12,2 s) |
| Fundraiser-Einschub | **60:36 bis 63:24** (168 s) |
| Ende abgeschnitten | ab Rohzeit 101:36 (11 Segmente) |

**Gegenprobe:** rechnerisches Inhaltsende 94:58 gegen gemessene
Dateilaenge 94:58.

**4 Segmente vorn und 11 hinten sind weggefallen**, weil sie
im Schnitt nicht vorkommen. Die Rohfassung steht unveraendert in
`aaronson-roh.transkript.md`.

**Ohne Sprecherzuordnung** — die drei Tonspuren trennen die Sprecher nicht
(Quartilsabstand 2,3–2,4 dB). Lieber keine Angabe als eine erfundene.

---

**[00:03]** I have. Decades ago, though.
**[00:05]** Great. Because that's basically me today.
**[00:09]** Out of every conversation I've got lined up these days with
**[00:13]** ex-NFL stars, UFC fighters, Navy SEALs,
**[00:17]** actors and Burning Man CEOs this one with you here is the one I've had the
**[00:24]** most nerves about and that's because it's because you're one of the world's
**[00:33]** leading authorities in your field right and I'm like the what well let's
**[00:39]** say the one and only F I ever got in my entire high school career was of all
**[00:46]** subjects in physics. I didn't study physics as a student. I studied math and
**[00:52]** computer science. I just sort of came into physics by a side door of
**[00:57]** quantum information. All right well at least you didn't have any other Fs.
**[01:01]** Well yeah to be fair I only passed my math classes because I was
**[01:05]** flirting with my very young math teacher all the time. But, good thing we got this.
**[01:10]** That clearly shows a different kind of talent.
**[01:13]** Right.
**[01:14]** Yeah.
**[01:15]** We got this out of the way. So today, I'm the idiot in the room and I'm weirdly excited
**[01:20]** about it. And I thought, you have two kids, right?
**[01:24]** I do.
**[01:25]** What age are they?
**[01:26]** They're 13 and 9.
**[01:27]** Okay. So, what have you been telling them when they ask you what daddy does for
**[01:32]** Oh, I mean, they know. They can say some of the basics about what's the P versus NP problem,
**[01:39]** what's quantum computing. To them, it's just normal. My wife is also a theoretical
**[01:45]** computer scientist, so that's kind of in the air in our house. But I've made it clear
**[01:52]** to the kids that I'm going to support them no matter what they choose to do, even
**[01:56]** if it's algebraic geometry, even if it's physics or engineering. It doesn't have to be theoretical
**[02:04]** computer science.
**[02:05]** But how do you start explaining to them what you do? Like one day away, let's say five
**[02:11]** years old.
**[02:12]** Well, okay. I mean, we do math for the purpose of understanding what are the ultimate
**[02:19]** limits of computers. What can you ever do or not do with computers? And as part of that,
**[02:28]** I study a new type of computer called a quantum computer that people are just starting now
**[02:33]** to be able to build, but which looks like it could do some things quickly that would
**[02:39]** take our current computers longer than the age of the universe. So they're interesting
**[02:45]** to me, because not so much because of the applications, although I hope they'll be useful
**[02:51]** for at least a few things, but just because they change the limit. They change the answer
**[02:55]** to that question of what is or isn't computable in our universe in any reasonable amount
**[03:00]** of time. And that's really what I'm after, is understanding the answer to that.
**[03:05]** What was your latest breakthrough?
**[03:07]** You know, I'm kind of on the downswing here, you know, I've gotten so much less capable
**[03:19]** at doing technical work than when I was younger.
**[03:23]** You know, I've shifted to a different mode, you could say, where I form out more and
**[03:27]** more work to my grad students, you know, and now, of course, to AIs, right, which,
**[03:32]** I'm sure we'll talk about that.
**[03:33]** But that's changing the entire nature of what we do.
**[03:37]** But some of the things that I've been involved with
**[03:40]** in the last couple of years that might interest you,
**[03:43]** I and others had theoretical proposals
**[03:47]** for things you could do with a quantum computer that
**[03:50]** would actually get an advantage over a classical computer
**[03:53]** that have now, just within the last year or two,
**[03:56]** turned into actual experiments.
**[03:58]** For example, this company, Quantinuo in Colorado,
**[04:02]** has done with its 100-qubit quantum computer.
**[04:05]** So one of these was called quantum information supremacy.
**[04:09]** And this was about doing something
**[04:12]** with a small number of qubits, quantum bits,
**[04:15]** like let's say 12 qubits, but that could only
**[04:19]** have been done with a much larger number of classical
**[04:22]** bits, several hundred, I think.
**[04:25]** And what's nice is that this separation was just provable,
**[04:29]** without having to make any assumptions about what
**[04:33]** are the limits of classical algorithms, which
**[04:35]** is something that we still can't prove a lot about.
**[04:40]** But if you're just comparing bits to qubits,
**[04:42]** then you actually can prove these things.
**[04:44]** And this led to an experiment that
**[04:46]** was just because of where the technology is now,
**[04:50]** It would not have been doable a few years ago, okay?
**[04:52]** But the experiment was doable now.
**[04:56]** And then another experiment which started from a proposal that I had back in 2018.
**[05:02]** And then we published a paper on it in 2023.
**[05:04]** And then just about a year ago was actually demonstrated
**[05:09]** in a collaboration between Continuum and JP Morgan Chase.
**[05:14]** And this was about using current quantum computers
**[05:18]** to generate cryptographically certified random bits.
**[05:21]** So, it's very easy to generate random numbers, right?
**[05:26]** Certainly if you have quantum mechanics, right?
**[05:29]** Randomness is just built in, right?
**[05:31]** In fact, if you just stuck a Geiger counter
**[05:33]** next to some radioactive material, right?
**[05:35]** The pattern of clicks when there's a decay, right?
**[05:38]** According to the known laws of physics
**[05:40]** going to be inherently random, right? Okay, but we were interested in a harder
**[05:46]** problem, right, which is how could you generate random bits, you know, publish
**[05:51]** them on the internet and then prove to every skeptic that these bits really
**[05:55]** are random, right? What are the practical implications for everyday life?
**[05:59]** Yeah, well, okay, so having a certifiable randomness source could be
**[06:04]** useful for several kinds of cryptographic protocols okay the easiest
**[06:09]** one to explain would be cryptocurrencies okay especially proof of
**[06:13]** state cryptocurrencies like aetherium now is since they did this merge a year
**[06:19]** or two ago right so you know a proof of state cryptocurrency is way more
**[06:25]** environmentally friendly than Bitcoin like you're not using a significant
**[06:29]** fraction of all the electricity in the world to just you know do these useless
**[06:34]** computations okay but what you do need is you need to constantly run a lottery
**[06:40]** to decide who gets to add the next block to your blockchain right and so
**[06:45]** and so you know billions of dollars are riding on this everyone needs to
**[06:49]** trust that this lottery is fair okay and so so this is this is you know
**[06:53]** Right now, they do it in some more ad hoc way.
**[06:57]** They sort of, I think, source the randomness from the blockchain itself.
**[07:01]** But if you wanted a sort of really physically rooted source of randomness, then our proposal
**[07:08]** was you could actually use current quantum computers for this.
**[07:13]** And the basic protocol, by the way, this is the only thing in my career that I've
**[07:18]** patented so far, you know, through UT Austin, and we even licensed it for a while, you know,
**[07:25]** no one's gotten rich from this patent, but the basic proposal is that you have a classical
**[07:32]** challenger, you know, with a very small amount of seed randomness, and then that challenger
**[07:37]** uses their seed to generate a quantum circuit, so like a sequence of operations that a quantum
**[07:46]** computer could apply, which looks random, it's not really, it's pseudo-random.
**[07:52]** But then you could think of my protocol as a way of bootstrapping from that pseudo-randomness
**[07:58]** into true randomness.
**[08:00]** Because what's going to happen is that the pseudo-random circuit gets sent over
**[08:04]** to the quantum computer, let's say just over the internet, and now the quantum
**[08:08]** computer is challenged. It has to respond by you're running the circuit
**[08:12]** and then sampling some of the outputs that you get by running it, right? Which
**[08:16]** you're just going to be strings of ones and zeros, right? Like if it's a 50
**[08:21]** qubit circuit then you know each time you measure you'll see a string of 50
**[08:24]** bits, okay? So you just say send me some of these strings, right? And then
**[08:30]** Then the classical verifier, at its leisure, can do a statistical test on those shrigs
**[08:38]** to check, are they actually consistent with having been output by this circuit?
**[08:44]** This is actually the bottleneck in my whole protocol, interestingly.
**[08:47]** It's not the quantum computation.
**[08:49]** It's the classical verification of the quantum computation, which seems to take like
**[08:56]** two to the fiftieth time, right, if it's 50 qubits. Or, you know, and that's the
**[09:00]** reason why you probably want to stop at about 50 qubits, right, because if you did
**[09:04]** it with a hundred qubits, now you're talking about two to the hundredth time,
**[09:07]** right. You know, and we do have supercomputers today that can do two
**[09:10]** to the fifty. We don't have ones that can do two to the hundred, okay. So,
**[09:15]** so, so it is, it is bottlenecked in that way, okay, but, you know, at your
**[09:20]** leisure, you can do this verification. And here's the key point. If it checks out, then I can,
**[09:28]** my post-doc, Shi-han Hung and I, were able to prove that under some plausible cryptographic
**[09:36]** assumptions, even a quantum computer could have only generated these samples quickly if it is
**[09:42]** is really sampling them from a distribution that
**[09:45]** has a lot of real randomness in it.
**[09:47]** So the point is you don't have to trust the quantum computer.
**[09:50]** The quantum computer could have been
**[09:51]** commandeered by the NSA, or by Chinese intelligence,
**[09:56]** or by whoever your worst enemy is.
**[09:59]** But if they're sending you samples
**[10:01]** that pass the statistical test,
**[10:03]** then either we're just totally wrong about what
**[10:08]** problems are hard for quantum computers,
**[10:10]** or else there must be real randomness in those samples,
**[10:14]** a lot of it.
**[10:15]** And you can then feed the samples
**[10:18]** into a classical algorithm that's
**[10:20]** called a randomness extractor.
**[10:23]** This is just known stuff in computer science.
**[10:25]** But you can extract from that nearly uniform random bits,
**[10:29]** which you can then use for all sorts
**[10:31]** of cryptographic applications.
**[10:33]** So those are some examples of some of the work
**[10:36]** that I've done over the past decade.
**[10:39]** I'm also super fascinated by your personal story
**[10:42]** because I think you're the only person I've heard of
**[10:44]** that dropped out of high school,
**[10:45]** dropped out of high school at the age of 15
**[10:48]** in order to go to college.
**[10:51]** And-
**[10:52]** Well, I mean, drop out is one way of putting it.
**[10:54]** I got a New York State GED when I was 15,
**[10:58]** No, basically I didn't like the environment of high school, either intellectually or socially.
**[11:08]** No, I resonate with that.
**[11:10]** Yeah, yeah, yeah. And I wanted to get out. And I had always been ahead in math,
**[11:14]** and so I just sort of used that as an excuse, sort of, to just get out quicker.
**[11:19]** I had a very unusual circumstance, which was that my father was working in Hong Kong for a couple of years.
**[11:26]** So I lived in Hong Kong when I was 13. So I was moving back and forth between the U.S. and Hong Kong.
**[11:32]** And so it was like completely different school systems.
**[11:35]** And I sort of took advantage of the differences to say,
**[11:38]** well, you know, actually for me to be doing the math that I should be doing, you know,
**[11:42]** actually I should be in ninth grade instead of eighth grade.
**[11:45]** And then when I came back to the U.S. it was 11th grade instead of 10th grade, right?
**[11:49]** And then after that I found out, I had sort of run out of math at my high school,
**[11:55]** but I found out about a program at Clarkson University in upstate New York,
**[11:59]** which was called the Clarkson School, where just high school seniors can,
**[12:04]** you know, take college courses and they get their high school diploma
**[12:09]** and then they can transfer to a different college.
**[12:12]** So I did that when I was 15.
**[12:16]** That was a nice experience.
**[12:18]** And then applied to a lot of colleges,
**[12:21]** got rejected from almost all of them.
**[12:24]** But Cornell was kind enough to accept me.
**[12:27]** So then I went to Cornell when I was 16.
**[12:30]** And I've wondered, should I have done this or not?
**[12:35]** Professionally, I'm very happy that I did it.
**[12:38]** And I would do it again.
**[12:39]** I think many, many more kids into math and science
**[12:45]** could be doing this if we were set up to do it.
**[12:49]** I wish that people were able to move more at their own pace
**[12:53]** through the curriculum.
**[12:54]** I feel very strongly about that.
**[12:57]** And I'm dealing with that now with my own kids.
**[13:00]** So that I have no regrets about at all.
**[13:04]** Socially, it made dating a hell of a lot harder.
**[13:08]** How so?
**[13:09]** Well, I was three years younger than my classmates.
**[13:13]** And so it took me a long time to learn
**[13:22]** how to simulate a person with normal social skills.
**[13:25]** So I really needed to be playing on easy mode,
**[13:28]** and I was playing on hard mode.
**[13:30]** But so, you know, I do think it's easier for girls than for boys, you know, to do this.
**[13:37]** You tricked the system, basically, and then went on to work at MIT for nine years and
**[13:42]** Well, there were steps in between, yeah.
**[13:44]** I mean, I went to, after Cornell, I went to Berkeley for grad school.
**[13:48]** I was there for four years, and then I was a postdoc at the Institute for Advanced
**[13:53]** study in Princeton and then for two years at the University of Waterloo in
**[13:58]** Canada and then I got hired by MIT as a professor yeah and then I was there for
**[14:02]** nine years and then you know that there I got married we had our daughter but
**[14:08]** then my wife and I needed jobs in the same place and we ended up having a
**[14:13]** very nice offer here in Texas and so we moved here a decade ago. When did
**[14:17]** How did you develop this passion, I want to say obsession with quantum computing?
**[14:22]** Well, yeah, that was not how I got into computer science in the first place.
**[14:29]** I found out what programming was when I was 11, let's say, and I was just devastated
**[14:35]** that no one had told me about it before.
**[14:39]** I had dreamed of making my own Nintendo games.
**[14:42]** very into Nintendo, as probably most kids were
**[14:46]** in the 80s and 90s.
**[14:49]** But I had no idea even what sort of thing
**[14:54]** would be involved in making Zelda or Mario.
**[14:57]** Would you go to a factory and how do you make
**[15:01]** the characters move in exactly the way you want?
**[15:06]** And it was a revelation when a friend
**[15:09]** showed me, this was actually Apple Basic, okay, so, you know, truly, truly ancient,
**[15:14]** you know, programming language, but, you know, the point was, you know, here's this spaceship
**[15:20]** game or whatever, and here are these lines of code, right, and the lines of code are
**[15:24]** the complete specification of the game, you know, you want the game to do something
**[15:28]** different, you just have to change the code, right, and you know, I like to say,
**[15:31]** me that was like finding out where babies come from. It was just revelatory. So I wanted
**[15:39]** to learn all I could about programming. In seventh grade I found a friend who was also
**[15:46]** into it, in fact a much better programmer than I was. We made shareware games together.
**[15:51]** I think we put them on America Online. I think we made at least $30 from people
**[15:57]** registering our shareware.
**[15:59]** But I also realized that I was, even if I liked programming,
**[16:06]** I was not good at software engineering.
**[16:09]** I liked making my code work with other people's code,
**[16:13]** getting it done by a deadline, documenting it.
**[16:16]** Of course, now we have AI to help do all that stuff.
**[16:21]** Back then, we certainly didn't.
**[16:22]** And I got more and more drawn to the mathematical side of it,
**[16:28]** just understanding what kinds of programs
**[16:30]** could ever be written, what kinds of problems
**[16:33]** could or couldn't be solved by any program.
**[16:35]** And I got very interested in these programming languages
**[16:40]** that I was learning, which were, at the time,
**[16:43]** basic, and then Pascal, and then C, and C++, and Java.
**[16:49]** Are these the limit of what you can do?
**[16:51]** Could there be some other programming language that would let you do things that could never
**[16:54]** be done in basic, let's say, even in principle, right?
**[16:59]** These are completely strange terms to me.
**[17:01]** Okay, you've heard of these programming languages, no?
**[17:04]** Like basic Java?
**[17:05]** No.
**[17:06]** Okay.
**[17:07]** I mean these are...
**[17:08]** Yeah, I've heard of Java.
**[17:08]** Yeah, okay, yeah.
**[17:09]** Yeah, I mean these are the...
**[17:10]** I mean some of these languages you may not have heard of just because they're
**[17:13]** old.
**[17:14]** Yeah.
**[17:15]** fashion decades ago, like Pascal, for example, right?
**[17:18]** But nowadays, a lot of people use Python, right?
**[17:22]** Back then, Python hadn't even been invented yet, okay?
**[17:25]** But, you know, I was-
**[17:26]** That was in the 19th-
**[17:27]** Yeah, this was, no, this was the 90s.
**[17:30]** This was the 90s.
**[17:31]** And so the question was,
**[17:36]** could someday someone make a new programming language
**[17:40]** programming language that would let you create a game that just never could be
**[17:44]** created in our existing languages for some fundamental reason right and so it
**[17:49]** was really a further revelation to me when I learned of something called the
**[17:53]** church touring thesis right and this was what Alan touring you know they
**[17:57]** sort of founder of computer science you know and his friends figured out
**[18:01]** back in the 1930s and it basically says that once you have enough
**[18:05]** functionality in your computer, you know, so you have the ability to do, you know,
**[18:11]** if-then, you know, conditionals, go into loops, right, you know, branch, you know,
**[18:16]** based on, you know, whether there's a zero or a one written somewhere, and you
**[18:21]** can read from a memory, you can write to a memory, right, you can use more
**[18:24]** and more memory, address different parts of the memory. At this point, you've
**[18:29]** basically cross this threshold of universality, okay, and you can, at this
**[18:34]** point, you can, you know, you're what's called touring universal, so you can do
**[18:39]** anything that could be done in any other programming language that we know,
**[18:43]** right, and the only questions are now just how much time do you have, how much
**[18:47]** memory do you have, right, so you could say like ever since the 30s and 40s,
**[18:52]** you know, our computers have gotten exponentially more powerful, right, but
**[18:56]** But they've gotten more powerful simply because they get faster and faster, and they get more
**[19:02]** and more memory, and we get more and more of them, but that's it.
**[19:06]** The basic principles of how they operate haven't changed at all, and so that was really huge.
**[19:13]** So the quantity is just...
**[19:15]** Yes, right.
**[19:16]** It's like the quantity has been going up exponentially.
**[19:19]** You know, that's Moore's law, right?
**[19:21]** That, you know, computing power,
**[19:23]** under all different ways of measuring it,
**[19:24]** has been doubling, you know, every 18 months,
**[19:26]** or every two years, or, you know, something like that.
**[19:29]** And, you know, that's been true,
**[19:30]** basically, from the 1950s until today, right?
**[19:33]** And that has really been the force that has powered,
**[19:36]** you know, most of the technological change
**[19:38]** that we've seen over that time, right?
**[19:40]** That's what got us from the ENIAC and so forth,
**[19:43]** you know, to the iPhone, you know,
**[19:45]** and now to the data centers that run CHAT, GPT, and CLAWD,
**[19:49]** and so forth, so much of it has just been this Moore's Law.
**[19:54]** But in some sense, it's all just been the same slug
**[19:58]** to a theorist or to a mathematician.
**[20:00]** It's all been the same operating principles,
**[20:03]** the same kinds of instruction sets,
**[20:05]** just more and more of it.
**[20:08]** And so then that really became part of my worldview
**[20:12]** that, in some sense, even if I wanted
**[20:15]** to understand this universe, I didn't necessarily
**[20:19]** need to know that much about physics.
**[20:22]** Physics is just kind of like an encoding detail.
**[20:24]** Like, OK, maybe the neutrino or the muon
**[20:31]** has this mass instead of that mass.
**[20:34]** But these are, no matter what the details of physics
**[20:37]** turned out to be, it would just be another
**[20:39]** touring universal programming environment.
**[20:42]** So you're basically saying there's still some hope
**[20:44]** for me to become a quantum physicist one day.
**[20:46]** Well, again, I'm telling the story
**[20:49]** of how I kind of got to it from the side door.
**[20:51]** I mean, I did take some physics in college,
**[20:54]** but in physics, things go very, very quickly
**[20:58]** to doing calculations with differential equations.
**[21:02]** We have infinitely many degrees of freedom.
**[21:05]** And then because that's too complicated,
**[21:08]** you then resort to a lot of often unjustified
**[21:12]** approximations.
**[21:13]** And people get really, really, really good at that.
**[21:16]** But that was just never the kind of math
**[21:18]** that resonated for me.
**[21:20]** I just wanted everything to be well-defined.
**[21:22]** I liked it when things were finite,
**[21:25]** or at least finite dimensional, right?
**[21:28]** And so I kind of kept physics at arm's length a little bit.
**[21:33]** Right, and I said, okay, it's just gonna be
**[21:35]** touring equivalent anyway to things that I do know, right?
**[21:39]** And so you could say, if you really believe
**[21:42]** that the world, in some sense,
**[21:44]** might as well be a big video game,
**[21:46]** a big computer simulation, right?
**[21:48]** then do you really care about exactly what instruction set
**[21:52]** it's running on?
**[21:52]** Or if the great programmer in the sky
**[21:56]** were using Pascal versus C or something.
**[22:01]** The whole point is that we know that all these things
**[22:03]** can emulate each other, right?
**[22:06]** But then it was really a further revelation
**[22:08]** when I found out about quantum computing.
**[22:10]** So this was the mid-90s,
**[22:13]** which was when sort of the most famous
**[22:14]** quantum algorithms were discovered, like Shor's algorithm for factoring, Grover's algorithm
**[22:20]** for search.
**[22:21]** And so I read popular articles about these things, you know, in 1995 or 96, and, you
**[22:27]** know, the popular articles kind of mis-explained it, you know, the same way that they often
**[22:33]** still mis-explain it 30 years later, right, which is, you know, what they always want
**[22:36]** to say is well a quantum computer would just be able to try every possible
**[22:42]** solution at once right and that's what would let it solve all these difficult
**[22:45]** problems exponentially faster than a classical computer right and I remember
**[22:50]** reading that you know as a teenager and I remember thinking you know this
**[22:53]** sounds like garbage this sounds like you know physicists who just don't
**[22:57]** understand what they're up against like they don't understand you know
**[23:00]** the limits of Turing computation.
**[23:04]** But of course, to be sure, I had to learn something
**[23:07]** about what is this quantum mechanics.
**[23:10]** And already in the 90s, the web was fairly new.
**[23:14]** But there were web pages explaining quantum computing,
**[23:17]** explaining these quantum algorithms that had just
**[23:20]** been discovered.
**[23:21]** So I read them, and I read the early quantum computing
**[23:25]** papers.
**[23:26]** And it was amazing to me just how little physics
**[23:31]** I needed to know to learn this.
**[23:33]** It's just vectors and matrices.
**[23:36]** It's just linear algebra.
**[23:39]** OK, you have to know what a complex number is.
**[23:41]** You have to know what a matrix is.
**[23:43]** But I knew enough math that I knew those things.
**[23:47]** And then just like you could have a virtuoso programmer who
**[23:54]** has no idea how a transistor works
**[23:57]** or what is actually going on at the hardware
**[24:00]** level of the machine, the whole point of modern computer
**[24:04]** science is that we create these abstraction boundaries.
**[24:07]** So you can think entirely in terms of your Python code
**[24:13]** Or maybe you descend to a lower level of the assembly code.
**[24:17]** But to be a programmer, you don't
**[24:21]** have to know how to build a transistor.
**[24:24]** That's someone else's problem.
**[24:26]** And it's the same way with quantum computing.
**[24:29]** The engineers and physicists are still
**[24:31]** trying to solve the problem of how do we actually
**[24:33]** make these qubits work at scale.
**[24:36]** They've made an enormous amount of progress on it.
**[24:38]** since I was first reading about this 30 years ago.
**[24:42]** They're still not where we want to be.
**[24:44]** But in the meantime, we are perfectly free to say,
**[24:48]** well, assume that you have perfect qubits.
**[24:51]** Then that would lead to sort of a new model
**[24:53]** of what is efficiently computable.
**[24:58]** And it turns out, so you could ask,
**[25:01]** so does quantum mechanics overturn this church
**[25:04]** thesis that I was talking about before, does it actually change the answer to what is computable?
**[25:11]** It's a subtle story, because in terms of what can be computed at all, like in any amount
**[25:17]** of time, quantum mechanics doesn't change that at all.
**[25:20]** It's the same set of computable functions that we had before, and this is because
**[25:26]** anything you could do with a quantum computer, you could eventually do with a classical computer.
**[25:31]** But in terms of what can be done in a reasonable amount of time, or let's say with reasonable
**[25:36]** scaling like, you know, in a few minutes or maybe a few days, but not like longer than
**[25:42]** the age of the universe, right, quantum computing really does seem to change that.
**[25:49]** And it changes it in a sort of weirder way than any science fiction writer would
**[25:54]** have had the imagination to invent, right?
**[25:56]** It changed, basically, quantum mechanics,
**[25:59]** which we learned 100 years ago, literally 1926
**[26:03]** was when Schrodinger wrote down his equation.
**[26:06]** And it hasn't changed in all that time.
**[26:08]** It's been sort of the basic language of physics
**[26:12]** for a century now, arguably the most successful theory
**[26:17]** in the history of science.
**[26:20]** But also, famously, maybe the weirdest thing
**[26:23]** that science ever discovered.
**[26:24]** Because at its core, quantum mechanics
**[26:28]** is a change to the rules of probability themselves.
**[26:32]** And it replaced it.
**[26:35]** In normal life, we could talk about numbers from 0 to 1
**[26:40]** that quantify, I think this person has a 30% chance
**[26:44]** to win this election or an 80% chance.
**[26:47]** I would never say a negative 30% chance.
**[26:49]** That would be nonsense.
**[26:50]** And even less would I say a square root of minus 1% chance.
**[26:54]** But in quantum mechanics, I have to give every possibility
**[26:57]** a number called an amplitude.
**[26:59]** These amplitudes can be positive or negative, or even complex numbers.
**[27:04]** And so then there's a whole new calculus
**[27:06]** for how you deal with these amplitudes, how they evolve in time.
**[27:10]** They can cancel each other out.
**[27:12]** So if something can happen one way with a positive amplitude
**[27:15]** and a different way with a negative amplitude,
**[27:18]** then the total amplitude could be zero,
**[27:20]** so that the thing never happens at all.
**[27:21]** This is called quantum interference.
**[27:24]** And then there's a rule for what happens when you look,
**[27:27]** when you make a measurement.
**[27:28]** And then these amplitudes turn into
**[27:31]** ordinary probabilities,
**[27:33]** that you'll see one thing versus another thing.
**[27:35]** But the way that we calculate those probabilities
**[27:38]** is now totally different
**[27:39]** from anything in our everyday experience.
**[27:42]** So that's basically what quantum mechanics is all about.
**[27:46]** And no one had ever explained that to me.
**[27:48]** I had read popular books, and they said all kinds of things.
**[27:52]** Quantum mechanics is weird.
**[27:54]** It says particles are not in any one place.
**[27:57]** They're in a kind of smear of probability wave.
**[28:00]** And I would read that, and I would be like,
**[28:02]** well, isn't that just a fancy way of saying
**[28:04]** that you don't know where the particle is?
**[28:06]** I mean, this is exactly.
**[28:07]** I think at some point you just have to come out with it
**[28:09]** and say, look, it's about these amplitudes.
**[28:12]** It's about this change to the rules of probability.
**[28:15]** So that's what I learned when I started reading
**[28:17]** about quantum computing as a teenager.
**[28:19]** And you know, that's how I got into it.
**[28:22]** Yeah, I think this is the very first prop explanation
**[28:24]** I got about quantum physics.
**[28:26]** And you mentioned ChetGPT.
**[28:29]** So fast forward in your career,
**[28:31]** you also worked two years at ChetGPT,
**[28:34]** at OpenAI on the foundations of AI safety.
**[28:39]** What exactly was your job there?
**[28:40]** All right, so yes.
**[28:42]** Now we're getting to the juicy stuff.
**[28:44]** Yeah, yeah, and this is a big fast forward,
**[28:47]** but no, I could say actually I got into
**[28:53]** quantum computing in the late 90s
**[28:55]** when I was still an undergrad at Cornell,
**[28:59]** But, you know, I still wasn't sure whether I would ever be able to do anything original
**[29:05]** in that, right?
**[29:06]** And I was also very, very interested at the time in AI and machine learning, right?
**[29:12]** Which were another, you know, big part of computer science and, you know, where clearly
**[29:17]** exciting things were happening.
**[29:19]** And, you know, already then I could see like this, you know, this AI stuff probably
**[29:24]** it will impact the real world on a shorter time scale than quantum computing.
**[29:28]** When was that?
**[29:29]** This was the late 90s.
**[29:30]** Oh, wow.
**[29:31]** Yeah, yeah, yeah.
**[29:32]** AI was a thing already?
**[29:33]** I mean, the term AI was coined in 1956, right?
**[29:38]** So there's this whole prehistory of, you know, Marvin Minsky and, you know, all
**[29:46]** these actually, you know, very great thinkers, right?
**[29:51]** but you know they spent an enormous amount of time on approaches that
**[29:55]** didn't really work right and you know and again and again they felt like okay
**[30:00]** if we could just introspect enough and if we could just understand the nature
**[30:04]** of our own cognition you know then we could figure out how to just describe
**[30:07]** it to a machine and you know actually John McCarthy who was another of the
**[30:11]** pioneers of AI said like if we ever figure it out you know how much
**[30:15]** computing power you have will be totally irrelevant. We could run a human level AI
**[30:21]** on the computers from the 60s, okay? And what no one wanted to believe was that
**[30:27]** it would just be a matter of getting a massive amount of computer power and
**[30:31]** feeding in a massive amount of training data and then it would all
**[30:35]** just start to work for some, you know, totally inscrutable reason, right?
**[30:39]** That hypothesis was around, okay, but it was just too ugly to take seriously
**[30:45]** Right. No one wanted hardly anyone wanted that to be true, right?
**[30:49]** And and also they didn't believe it was true, right?
**[30:52]** It just it just seemed like magical thinking so when the real breakthrough happened with well again
**[30:57]** You know, it wasn't so much a kid. Okay
**[30:59]** I mean you could say the conceptual breakthroughs right those have already happened like the 1970s the 1980s
**[31:05]** right, people had the idea of neural networks, you know, already then, okay?
**[31:10]** You know, when people talk about deep learning today, that's just a rebranding
**[31:13]** of neural networks, okay? You know, we're talking about the same thing, okay? So
**[31:18]** people, you know, neural nets go back, I mean, you know, actually they
**[31:22]** originated in the 1940s, and then it becomes something called the Perceptron
**[31:26]** in the 1960s, and then, you know, by the 1980s, you know, you have people
**[31:30]** actually, you know, training multilayer neural nets. So in some sense they have
**[31:35]** all the right ideas. You know, what they don't have is nearly enough computer
**[31:40]** power or training data, right? You know, and like they're short by
**[31:45]** like factors of millions, right? And so it looks like, you know, these are
**[31:49]** just kind of not-so-great ideas that don't really work, right? That, you
**[31:54]** you know, that was how it seemed at the time, right?
**[31:57]** And you had to be like, you know, in some sense,
**[31:59]** a really crazy person to say, no, you know, just you wait.
**[32:02]** If you scale up this non-working idea
**[32:05]** by a factor of millions,
**[32:06]** then suddenly it's going to start working, okay?
**[32:09]** A few people said that, okay?
**[32:11]** But you know, now here we are, you know,
**[32:15]** some decades later, and I think it's safe to say,
**[32:17]** that is what happened.
**[32:18]** Where would you, if you trace it back, what would you say, when did the breakthrough happen?
**[32:25]** Well, okay, so again, you're looking for a conceptual breakthrough that I'm telling you was not there, right?
**[32:31]** I mean, there was a, you could say that there were conceptual breakthroughs back in the 40s, the 60s, 70s and 80s
**[32:40]** and coming up with these neural nets, figuring out how to train them.
**[32:43]** But then, you know, they still didn't work for decades because it turns out that to get
**[32:48]** an impressive result, you needed, you know, a neural net with billions of neurons, right?
**[32:53]** And you needed an amount of training data that was, like, on the scale of, like, all
**[32:58]** the stuff on the entire internet, right?
**[33:01]** You know, and then at that point, it starts showing all this human-level intelligence,
**[33:05]** right?
**[33:06]** But not before that.
**[33:07]** Okay.
**[33:08]** I see.
**[33:09]** I see.
**[33:10]** And this was so weird that again, when I started in computer science, almost no one
**[33:15]** would have expected this was possible.
**[33:17]** It was obvious to everyone that you would need some further breakthrough.
**[33:21]** But no, mostly it was just massively more computer power and data.
**[33:27]** What was your job at OpenAI?
**[33:31]** So after choosing not to go into AI, choosing
**[33:36]** to go into quantum computing back in 2000,
**[33:44]** even though AI seemed exciting, it seemed like all the progress
**[33:49]** that people were making was almost entirely empirical.
**[33:53]** First of all, of course, it didn't work then, nearly like it works today.
**[33:57]** But even to the extent that it did work,
**[34:00]** no one really understood why it worked.
**[34:02]** It's like you could write papers with some bar charts
**[34:05]** in them that says, OK, we tried this machine learning
**[34:10]** method on this benchmark suite,
**[34:13]** and here were the results.
**[34:14]** And doing this made it 20% more accurate.
**[34:17]** But I like to sit back and really, really understand
**[34:22]** why something is working.
**[34:24]** And so I found more of that in quantum computing.
**[34:28]** But then in the decades that I was not an AI, of course,
**[34:32]** it did get better and better, driven in large part
**[34:35]** by these massive advances, massive increases
**[34:39]** that we got in computing power and data.
**[34:43]** There were some new ideas.
**[34:45]** So there was a particular architecture for neural nets
**[34:49]** that was invented in 2017 called the transformer, okay?
**[34:52]** And that was a big enabler for everything that happened.
**[34:55]** So if you had to pick a breakthrough that was recent,
**[34:59]** you could have picked the transformer in 2017,
**[35:02]** which came out of a team at Google.
**[35:04]** Now, my guess is-
**[35:05]** Which is the T in GPT, by the way.
**[35:08]** Yeah, that's right.
**[35:09]** It's a generative pre-trained transformer.
**[35:12]** That's right.
**[35:13]** It's referring to this just particular type of neural net.
**[35:16]** Now my best guess is that if the transformer
**[35:19]** hadn't been invented, it would have been a few more years
**[35:21]** and then we would have gotten to the same place.
**[35:23]** But, you know, but that did accelerate things, okay?
**[35:27]** So anyway, so I was aware that, you know,
**[35:32]** some impressive things were happening in AI.
**[35:34]** You know, in 2011, we saw the computer
**[35:38]** beat the human champion in Jeopardy, right?
**[35:40]** In 2016, we saw a computer beat the human champion at Go,
**[35:45]** right, and then, you know, we saw, like,
**[35:48]** some really impressive results at classifying images.
**[35:52]** In 2020, in 2021, you know,
**[35:55]** almost everyone was distracted by the pandemic,
**[35:57]** but, you know, I saw, you know,
**[35:58]** there was this weird little outfit called OpenAI
**[36:02]** that was putting out this thing called GPT, right?
**[36:05]** This was before a chat GPT, right?
**[36:07]** But I was able to try out this GPT-3.
**[36:12]** And I could see, yes, this really
**[36:14]** is a step change compared to anything that's come before.
**[36:17]** This is not just like a sort of trivial chatbot of the type
**[36:24]** that we had since the 60s.
**[36:26]** There was this thing called ELISA that just basically
**[36:30]** just sort of rephrases whatever you say to it, right?
**[36:33]** And so it's like, it's the illusion
**[36:35]** of a conversational intelligence,
**[36:37]** but really no one's at home there, right?
**[36:39]** And so when people first heard about GPT,
**[36:42]** especially in computer science and in linguistics,
**[36:45]** think overwhelmingly their reaction was,
**[36:47]** this sounds like just another ELISA.
**[36:49]** It sounds like just another parlor trick, basically.
**[36:54]** But I tried it out and I could see,
**[36:56]** No, this is not a Liza, you know.
**[36:58]** What did it look like in these early days?
**[37:00]** So there was this thing called AI dungeon
**[37:03]** that you could use where you could just type something
**[37:07]** and you could start writing a story, it would continue it.
**[37:11]** So it was not yet good enough to be useful, I would say.
**[37:14]** But it was good enough to be interesting.
**[37:17]** It was clearly trying to continue whatever you wrote.
**[37:21]** Sometimes it would get off topic, right?
**[37:24]** It wasn't like reliably answering your question.
**[37:27]** But, you know, there was clearly like some kind of model
**[37:31]** inside of it, you know, of the world, right?
**[37:34]** Of what all these words and phrases actually meant,
**[37:38]** you know, that, you know, none of the earlier chatbots
**[37:40]** would have had anything like, right?
**[37:42]** So I could see, you could say like in some sense,
**[37:45]** I got AI-pilled in 2021 or so.
**[37:48]** Yeah, they converted you to the dark side.
**[37:49]** Yeah, well, no.
**[37:53]** I was like, OK, if this works just by training
**[37:59]** a big enough neural net, then all the computer scientists
**[38:02]** who said otherwise 20 years ago, they were all wrong.
**[38:07]** And as you keep scaling this up,
**[38:09]** we should expect it to just get better and better.
**[38:11]** So by that point, I have friends who
**[38:16]** would reach that realization much earlier,
**[38:18]** like a decade ago, before that.
**[38:20]** So I had no very good excuse.
**[38:22]** But OK, but I did realize that.
**[38:25]** There was still, I didn't know what I could be doing there.
**[38:29]** But then in 2022, Ilya Sutskofer,
**[38:33]** who was then the chief scientist at OpenAI,
**[38:36]** and it was the co-founder of it.
**[38:40]** And Jan Leicke, who was then the head of alignment at OpenAI,
**[38:47]** reached out to me, and they said, listen,
**[38:50]** we read your blog, we're fans of your blog, whatever,
**[38:54]** and we would like you to go on leave for a year
**[38:57]** and work in our AI alignment team.
**[39:01]** And my first reaction was like, why do you want me?
**[39:04]** I'm a quantum computing person.
**[39:05]** What you're doing has nothing to do with quantum computing.
**[39:08]** And I said, no, we think about it more broadly.
**[39:11]** You're a theoretical computer scientist.
**[39:14]** And we really think that a theoretical computer science
**[39:19]** might be at the core of how do we do this safely.
**[39:23]** It's true that most of the progress that's
**[39:25]** gotten AI to work so well has been empirical,
**[39:28]** has just been trial and error.
**[39:30]** but if we want to ensure that it's safe,
**[39:32]** that it's not gonna help people make chemical weapons,
**[39:36]** or it's not gonna plot against humans or whatever,
**[39:39]** then we need some kind of guarantee,
**[39:41]** and that means we need to think about theory, right?
**[39:44]** So I still wasn't sure,
**[39:46]** but I knew people were thinking about this.
**[39:48]** I had actually had a spectacular undergraduate at MIT
**[39:52]** named Paul Cristiano, who did quantum computing with me,
**[39:55]** but who then later went to open AI
**[39:58]** and who became one of the leaders
**[40:00]** of this AI alignment field, right?
**[40:02]** So because of Paul, you know, I knew
**[40:05]** that one could actually think in this intersection
**[40:07]** of theoretical computer science and AI alignment.
**[40:11]** And so I thought about it and they said,
**[40:13]** you know, again, and guess what?
**[40:14]** You don't even have to move to San Francisco.
**[40:17]** You can stay with your family in Austin,
**[40:19]** stay with your students.
**[40:20]** You'll just fly out to visit us once a month.
**[40:22]** and we'll just pay you and you won't have to teach.
**[40:27]** So they made it very hard to say no.
**[40:30]** What did your job actually look like?
**[40:31]** So there was never any very clear job description.
**[40:36]** It was try to use theoretical computer science
**[40:40]** to solve AI alignment basically.
**[40:43]** And so I looked for things to do,
**[40:47]** and actually I would have weekly meetings
**[40:49]** with Ilya, where I would say to him,
**[40:53]** like here, I've made some progress on this,
**[40:55]** I've made some progress on that,
**[40:57]** and Ilya would always say, okay, that's great, Scott,
**[40:59]** but what we really want from you
**[41:01]** is what is the mathematical definition,
**[41:03]** what it means for the AI to love humanity?
**[41:06]** And I would have to say,
**[41:08]** Ilya, I'm still thinking about that.
**[41:09]** I don't have a lot of progress to report on that.
**[41:12]** I'm not even sure how much of that is a math problem.
**[41:18]** It seems like there's 3,000 years of moral philosophy that is implicated in this question.
**[41:27]** My challenge, of course, is can I break off little bits and pieces of this that can be
**[41:31]** addressed mathematically because in the end I would like to make progress.
**[41:36]** The most concrete thing that I found to do when I was at OpenAI was I came up with the
**[41:42]** first scheme for watermarking the outputs of a large language model, like chat GPT or
**[41:48]** Claude or Gemini.
**[41:50]** What does watermarking mean?
**[41:52]** It means slightly changing the way that the language model works in a way that should
**[41:58]** not be noticeable at all by an ordinary user, but which is embedding a subtle
**[42:03]** statistical signal into the choice of words that are coming out that would
**[42:08]** let you later prove, you know, to very high confidence that, yes, this text did
**[42:13]** come not only from AI, but from this specific AI model. Okay? So, you know, I
**[42:20]** I had a sort of a holy crap moment when I realized that this was going to be needed
**[42:27]** in the summer of 2022, so four years ago.
**[42:32]** This was before chat GPT had come out.
**[42:35]** But I could already use GPT-4 internally within the open AI, and so I saw how good
**[42:45]** it was, in particular, I saw that it was perfectly capable of writing, let's say, high school
**[42:50]** essays or college essays. And I was like, every student in the world is going to want
**[42:55]** to use this to cheat on their homework, aren't they?
**[42:58]** Totally.
**[42:58]** Right? So, you know, I don't have such a great track record at like seeing decades
**[43:03]** into the future, right? I missed what AI scaling was going to do. For example,
**[43:08]** I also missed how popular Bitcoin was going to be, right, as many people did, I guess.
**[43:13]** But in this case, I was able to see six months ahead.
**[43:16]** Okay.
**[43:17]** So would you say, I write on Substack, and they recently partnered up with Pangram.
**[43:23]** Yeah, that's right.
**[43:24]** So is that one of the children of your work?
**[43:27]** Not exactly, no.
**[43:30]** So what quickly became clear is that there were several different approaches to how you
**[43:34]** could make AI text detectable, right? So one approach would be to just treat it
**[43:39]** as yet another AI problem, right? So we train a new neural net to just
**[43:44]** distinguish human text from AI text as well as it can. This is essentially what
**[43:48]** pangram does, and they do very, very well at it, okay? You know, and other
**[43:54]** people have done versions of this as well, right? Now, you know, a
**[43:58]** A pangram actually works better than many of us expected that that kind of thing would,
**[44:05]** but there's still some false positives.
**[44:08]** And one issue is if you're going to be accusing a student of cheating based on the output
**[44:14]** of your tool, then you better be really damn confident.
**[44:19]** You would like a rate of false positives that's well below 1%, I would say.
**[44:24]** So that's part of the issue.
**[44:26]** Now, a second approach that you could imagine
**[44:29]** is you could have the AI companies just log all the text
**[44:33]** that they ever generate.
**[44:35]** And then you could imagine letting people query them
**[44:38]** to say, did you ever generate this essay or not?
**[44:42]** Now, you could argue whether or not that appropriately
**[44:46]** preserves people's privacy.
**[44:49]** Even if it did, it would be hard to convince them
**[44:52]** that it does, right, is part of, like,
**[44:54]** I think people would really, like,
**[44:55]** some people would really feel an ick about that,
**[44:58]** that, like, their privacy is being compromised that way,
**[45:01]** right, and so that brings us to a third possibility,
**[45:03]** and this is what watermarking is, right.
**[45:06]** Watermarking, unlike pangram,
**[45:08]** requires slightly changing the way
**[45:10]** that the LLM itself operates, right.
**[45:14]** um, as I said, not in a way that's easy to detect, right? But basically what it does is it takes
**[45:20]** advantage of the fact that, you know, LLMs are inherently probabilistic in how they work, right?
**[45:27]** And we all see this, like if you feed the same prompt to chat GPT a bunch of times, you know,
**[45:33]** you can get a different response each time, right? Why? Because it is sampling the next token
**[45:38]** from a probability distribution, right?
**[45:40]** And the whole thing that that transformer neural net
**[45:43]** is doing is it's not calculating exactly
**[45:46]** what the next word should be,
**[45:47]** it's calculating probabilities
**[45:49]** for each possible next word, right?
**[45:51]** And then normally what you would do
**[45:53]** is you would just sample,
**[45:54]** repeatedly sample from that distribution
**[45:57]** and this is how chat GPT, for example,
**[46:00]** generates its responses, okay?
**[46:02]** But with watermarking, we say, well, what if instead we generated it
**[46:08]** pseudo-randomly?
**[46:11]** So we're going to generate the next word in a way that looks random.
**[46:15]** In fact, it looks like it came from exactly this distribution
**[46:19]** with these given probabilities.
**[46:22]** But in some very hard to detect way, we're
**[46:27]** going to be biasing things in favor of combinations of words, you know, that like
**[46:32]** get a high score, you know, according to some pseudo random function, right? And
**[46:37]** the fact that we did that will then be detectable later, right? So, you know, we
**[46:42]** also need a detection tool, right, which is not going to know these
**[46:45]** probabilities. It's not going to know the prompt that someone may have typed
**[46:49]** to get this this essay, it just has the text itself, right? And from that it has
**[46:54]** to say is the watermark here or not, right? But, you know, if we know the key
**[46:59]** of this pseudo-random function, then we can just look at all that
**[47:03]** combinations of, let's say, five or so consecutive words, you know, calculate
**[47:07]** the pseudo-random function for each of them, add up all the results, and if
**[47:12]** the result is above some threshold, then we could say, like, there is at
**[47:15]** most a point one percent chance that this score would have been this high by
**[47:20]** by random chance right so ninety nine point nine percent yes you know this
**[47:26]** watermark of this AI is there okay so that so that was the basic principle
**[47:30]** you know which I proposed in 2022 and I went and gave talks about it you
**[47:35]** know one thing that was surprising to people at the time they thought that
**[47:39]** there would have to be an inherent trade-off between watermarking and the
**[47:44]** quality of the output. So they said yeah like yeah maybe you can do this but if
**[47:48]** you change the probabilities then you're going to degrade the quality
**[47:51]** right and and you know so so what I was explained to them was no there's
**[47:56]** no such trade-off right no one will notice anything different right
**[47:59]** because you're just replacing this randomness by pseudo randomness okay
**[48:03]** So since then, people sort of massively improved the basic theory that I laid out.
**[48:11]** They published papers about it.
**[48:12]** I never even published a paper on it.
**[48:15]** By the time I thought of writing one, it was already obsolete.
**[48:18]** The AI world moves too fast for me.
**[48:22]** And now, actually, Google, DeepMind, and Anthropic have both actually deployed water
**[48:28]** market, very similar to what I proposed. Open AI still is not. On a more
**[48:34]** personal level, what did working inside this AI machinery do to
**[48:40]** your sense of the future and to the future of your children? Yeah, well so
**[48:45]** it certainly prompted me to think more about it. I mean,
**[48:49]** even if I hadn't worked for Open AI, this is changing
**[48:53]** everything that we do, right? Like it's impossible to work in a computer science
**[48:58]** department, or for that matter to work in any department at a university, or for that
**[49:03]** matter to work anywhere at all, right? And not be aware of how this is
**[49:07]** changing the world. You know, it certainly, you know, like it made a lot of the
**[49:11]** conversations more salient for me earlier, you know, than maybe they
**[49:17]** would have been otherwise. And you know how I felt? Like, you know, when
**[49:21]** When I was 11 or so, besides playing a lot of Nintendo, I spent a lot of time reading
**[49:27]** Isaac Asimov's robot novels.
**[49:31]** I was really into them and when I first got into programming, I thought, okay, what would
**[49:37]** be really cool to do?
**[49:38]** I just want to build an AI that will follow Asimov's three laws of robotics.
**[49:42]** How come no one else thought of doing that?
**[49:46]** I tried, I got a little bit stuck at the how do you make it intelligent part, okay?
**[49:55]** And then I started learning more about real computer science when I was a teenager, and
**[49:59]** I found out, no, actually computer science has nothing to do with this, right?
**[50:05]** It is so ridiculously far from building anything intelligent enough that it would
**[50:10]** would actually engage any of these questions
**[50:13]** that Asimov was writing about.
**[50:15]** That was just my science fiction fantasy of what it would be.
**[50:18]** And now I get to see what the real thing is.
**[50:21]** And then, OK, fast forward 30 years.
**[50:24]** I'm working at OpenAI.
**[50:26]** I'm having lunch with different teams in the cafeteria.
**[50:30]** And all the conversations feel like I'm
**[50:32]** living in an Isaac Asimov novel.
**[50:36]** how safe is AI? I'm worried I'm very worried about where this I mean I mean I
**[50:43]** feel like you know we are you know this is not just some cool consumer product
**[50:47]** right we are you know we have created you know the first ever form of verbal
**[50:52]** intelligence on earth other than our own yeah I heard you were saying yeah
**[50:56]** calling yourself an apocole optimist apocole optimist yeah that was the
**[51:00]** phrase from this from this movie that was this documentary that that's all I made
**[51:05]** but I mean yeah there is there is no obvious stopping principle right we are
**[51:12]** like oh it's able to do these jobs better than us but not those jobs
**[51:16]** right there is there is basically you know like like if what I would say is
**[51:22]** that if there is a wall that AI is going to hit like where it stops
**[51:26]** improving you know where like like sort of you know where it leaves plenty for
**[51:31]** humans to still do that's economically valuable no one has convincingly
**[51:36]** articulated where that wall is okay I would say at this point the burden is
**[51:41]** on them to explain where this wall is right because what we've seen in the
**[51:46]** last few years is that as you scale more and more as you add more
**[51:50]** inference time compute you know meaning like it's thinking it's looking things up
**[51:55]** on the internet and so forth before it answers you right as you add more more
**[51:59]** training data as you do more reinforcement learning it just gets
**[52:03]** better and better and better right so like three years ago I would say you
**[52:08]** know it was already like like you know it was it was able to like pass some
**[52:11]** high school exams you know which was cool but you could say okay but it's
**[52:15]** not doing any real research, right? It's, you know, clearly, you know, it's, you know,
**[52:20]** I could give it, you know, one of like my research problems and it's just, it's just
**[52:25]** spouting nonsense, like the same as, same way an overconfident freshman would do,
**[52:29]** right? And it's like you could point at it and laugh, right? Okay, but, but now
**[52:35]** where are we? Well, you know, as some of your listeners might have seen, just
**[52:40]** this summer we have started to see a large number of breakthroughs in pure
**[52:45]** math, in theoretical computer science, that have come partly or entirely from
**[52:50]** the use of AI models. We have seen solutions to long-standing open
**[52:55]** problems. There was problems of the famous mathematician Paul Erdős. One of
**[53:00]** them was called the unit distance conjecture. It was falsified by an
**[53:04]** open AI model. There are several problems that I've cared about in
**[53:11]** quantum computing theory and in computational complexity have now been
**[53:15]** solved by open AI models. An anthropic model just a few weeks ago
**[53:22]** made progress on the Riemann hypothesis which is one of the biggest
**[53:26]** unsolved problems in all of math. It didn't solve it but it made progress
**[53:31]** that humans have not made. So I think mathematicians and computer
**[53:39]** scientists like see all this and especially this summer you know they see
**[53:43]** the writing on the wall right they see that you know like yes maybe there
**[53:47]** will still be a role for us you know you know you know many of us
**[53:51]** selfishly hope that there will be but the whole nature of what we do is now
**[53:56]** changed beyond recognition right and when I look at like the new quantum
**[54:00]** computing papers you know every night on the preprint server on the archive I
**[54:05]** would say at least half of the papers that interest me like you know within
**[54:09]** the last month or so are saying you know yes you know we use GPT we used
**[54:14]** Claude you know you know it at least helped in doing the technical work
**[54:20]** In preparation for this conversation I re-read the essay AI 2027 and one of the scenarios
**[54:28]** they describe anticipates humanity going extinct.
**[54:33]** What are your thoughts on that?
**[54:33]** I think that is unfortunately within the set of possibilities.
**[54:37]** I mean you know where I'm not you know so there is this whole movement of you know
**[54:42]** Sometimes they're pejoratively called AI-doomers.
**[54:45]** But it's most associated with Eliezer Gidkowski, who
**[54:50]** is sort of the prophet of this movement.
**[54:52]** He's been talking about this for more than 20 years now.
**[54:57]** He just regarded it as obvious that if we
**[55:01]** continue building AI, it will become superhuman.
**[55:04]** And then at some point, it will be to us,
**[55:07]** as we are to orangutans or whatever.
**[55:10]** How well do orangutans fare in a human world?
**[55:13]** Well, he would say something even stronger than that.
**[55:18]** He would say, by default, this kills us.
**[55:20]** By default, unless we have some breakthrough in how
**[55:25]** to align this with human interests,
**[55:28]** whatever goal it has, it could probably better achieve
**[55:31]** that goal by transforming the earth
**[55:34]** into something very different from what it is
**[55:37]** than it can by leaving us around, right?
**[55:39]** So now, I would say I don't accept the arguments
**[55:45]** that that is, let's say, a default outcome.
**[55:48]** On the other hand, is it a possible outcome?
**[55:51]** Well, unfortunately, yes.
**[55:53]** I mean, again, people need to conceptualize
**[55:57]** what is happening right now is it's not another cool
**[56:00]** technology like the internet or like social media, right?
**[56:03]** This is like, it goes back to the evolution
**[56:06]** of the hominid brain, right?
**[56:08]** Where something new happened in the whole history of Earth.
**[56:13]** Now you have this verbal intelligence
**[56:15]** that can conceptualize things,
**[56:17]** that eventually could write things down,
**[56:20]** could ponder things, right?
**[56:21]** And now we have a new one, right?
**[56:23]** And now we have one that is not constrained in the way that we are by having brains that
**[56:29]** have to fit into these skulls, that have to fit through the birth canal when we're being
**[56:36]** born.
**[56:38]** It's not constrained by having to operate on the comparatively tiny amounts of energy
**[56:44]** that we get from our food.
**[56:47]** can just keep scaling this thing up. And anyone who's interacted with Fable or with GPT 5.6
**[56:54]** Pro can see that by many measures these things are already much more intelligent than they
**[56:59]** are.
**[57:00]** For sure. At this point in time, what's your personal take? Where do you see AI
**[57:06]** going in the next five to ten years?
**[57:09]** to some very, very weird and very scary places.
**[57:12]** I mean, I hope that we'll still be around.
**[57:16]** I mean, look, you could say in terms of putting my money
**[57:18]** where my mouth is, I mean, my kids still go to school.
**[57:23]** They're thinking in terms of going to college.
**[57:26]** I'm thinking in terms of what college will they go to.
**[57:30]** But certainly, it affects me on that personal level
**[57:34]** of like, you know, what do I tell my kids
**[57:38]** that will be useful to them in this world, right?
**[57:41]** What will be left for humans to do
**[57:44]** that will have any economic value?
**[57:47]** So I think the, you know,
**[57:50]** there's an enormous range of possible outcomes,
**[57:53]** and right now is the time when, you know,
**[57:55]** we need to sort of make our voices heard,
**[57:58]** you know, if we want to steer things
**[58:00]** toward the better outcomes, right?
**[58:02]** Like this is one of the most consequential moments
**[58:04]** in human history, really.
**[58:06]** Do we have any influence, really?
**[58:08]** Well, I mean, you know, I think, you know,
**[58:12]** not everyone has as much influence as Sam Altman has,
**[58:17]** or, you know, Dario Amadei, okay?
**[58:19]** But I think we all have some non-zero
**[58:21]** amount of influence, right?
**[58:23]** At the very least, you know, we can vote.
**[58:26]** we can make our opinions known.
**[58:29]** And some subset of people can contribute
**[58:33]** by thinking about how do we make this safe.
**[58:38]** There's a huge amount that needs
**[58:39]** to be done in AI safety, in AI governance.
**[58:46]** And I think that those things are still
**[58:48]** very, very underfunded relative to the need for them.
**[58:52]** So yeah, so I think you could imagine like better outcomes
**[58:59]** where, look, even if AI can do everything
**[59:03]** that we can do better than we can do it,
**[59:06]** that's not necessarily the end of the world, right?
**[59:09]** Like you could say lots and lots of people
**[59:12]** have long ago made peace with that, with OK, maybe
**[59:16]** they're not doing much of economic value, right?
**[59:18]** or maybe they can't write a novel or paint a painting
**[59:24]** or prove a theorem beyond what anyone else could do.
**[59:27]** But they still enjoy their lives.
**[59:29]** They enjoy their friends.
**[59:30]** They enjoy their hobbies.
**[59:32]** And so it might be that the small number of us
**[59:36]** who've just invested so much of our identity
**[59:39]** in can we prove a theorem that no one else can prove,
**[59:43]** but maybe we'll just need to get over ourselves.
**[59:45]** But then, of course, there's the much more basic economic issue.
**[59:56]** If we really have this world where AIs stay kind of like friendly golden retrievers, kind
**[60:05]** of like Claude or GPT mostly are these days, right, and so they stay pretty controllable.
**[60:18]** You could imagine this world where they bring us infinite wealth, right, or almost limitless
**[60:25]** material wealth.
**[60:26]** But then does that wealth all flow to a few AI companies or does it get shared by
**[60:32]** of humanity and of course of course I would prefer the latter yeah this yes
**[60:36]** [[ FUNDRAISER-EINSCHUB — Help me bring Man's Search for Meaning to life ]]
**[63:24]** [[ ENDE EINSCHUB — das Gespraech laeuft weiter ]]
**[63:25]** one quote I can't stop thinking about by Arthur Clarke maybe our role on this
**[63:30]** planet is not to worship God but to create him what are your thoughts on
**[63:35]** that yeah so so there's a famous saying that like the the ultimate you
**[63:40]** know Silicon Valley answer to you know does God exist is neither yes nor
**[63:44]** or no, it's not yet, right?
**[63:47]** So, you know, I mean, like, you know,
**[63:50]** when you're in, you know, when you spend time
**[63:52]** in these circles, like the San Francisco AI world,
**[63:55]** like, yeah, like there are constant jokes about,
**[63:59]** you know, are we, you know, creating God, right?
**[64:04]** You know, build, people have used terms
**[64:06]** like, you know, the sand god, right?
**[64:08]** as silicon microchips being derived from sand.
**[64:14]** So this is clearly not a, we could say if it is a god,
**[64:19]** then it clearly isn't one that meets
**[64:21]** all of the traditional religious conceptions.
**[64:24]** It wasn't there at the beginning of the universe.
**[64:28]** Does it love us?
**[64:29]** Well, maybe.
**[64:30]** If we program it to love us, then maybe it will.
**[64:34]** I mean, I think that we are headed for a form of intelligence
**[64:39]** that's sufficiently far beyond our intelligence
**[64:43]** that it will seem godlike to us.
**[64:45]** And maybe some people have already had this experience,
**[64:49]** just interacting with caring AIs.
**[64:51]** It feels like, OK, people have prayed to gods for millennia.
**[64:56]** Now for the first time, we have something kind of like one
**[64:59]** that actually answers, right?
**[65:02]** You know, now of course, you know,
**[65:05]** one should be very cautious here, right?
**[65:08]** You know, we don't want, you know,
**[65:10]** we want people to maintain their critical faculties,
**[65:13]** right, and part of the problem is like,
**[65:15]** precisely because these models are now so good, right?
**[65:18]** It is so tempting to just forget your critical faculties,
**[65:22]** right, just believe whatever it's telling you, right?
**[65:26]** And that way lies a great deal of danger, right?
**[65:29]** So I think, look, I use LLMs for all sorts of things.
**[65:34]** I use it for...
**[65:34]** I heard you calling GPT-5.6 the greatest therapist
**[65:38]** of all time.
**[65:38]** Yeah, yeah, yeah.
**[65:39]** I mean, I can use it for just dealing
**[65:41]** with my personal traumas that are still with me
**[65:45]** from when I was this little kid
**[65:48]** who would skip grades in college, right?
**[65:50]** I can use it for just all kinds of personal issues.
**[65:54]** I can use it for my research, right?
**[65:56]** So, and so many other people have found
**[66:05]** so many other uses for it, right?
**[66:07]** But yes, one should also remember
**[66:10]** that these are not literally gods.
**[66:13]** They are also consumer products, right?
**[66:15]** they've been shaped by a whole bunch
**[66:18]** of different incentives, right?
**[66:19]** Including commercial incentives
**[66:22]** that to make people want to keep using them.
**[66:25]** And so I think it is really crucial
**[66:29]** that even as we use them,
**[66:31]** that we don't completely lose our critical sense
**[66:35]** or our ability to evaluate things for ourselves.
**[66:38]** And that's, I'm a professor, right?
**[66:41]** this is a huge problem that we're facing right now in education, right?
**[66:45]** How do we convince our students to maintain their ability to think things through for themselves?
**[66:51]** Yeah.
**[66:53]** Speaking of God, I was fascinated by the fact while prepping this conversation
**[66:59]** that, to me, you are unique in the way that, you know, you are...
**[67:06]** You've been working in this space of science for decades, and at the same time you write
**[67:14]** about spirituality, religion, even existentialism a lot.
**[67:19]** I mean a little bit.
**[67:21]** I write about sort of whatever is interesting to me at the moment, or whatever is helping
**[67:27]** me procrastinate from whatever else I should be doing, right? But I mean, you know, clearly,
**[67:35]** you know, religion, art, you know, these are all parts of human experience. And, you know,
**[67:40]** if you're interested in everything, then of course you're going to be interested
**[67:43]** in them.
**[67:44]** What do you believe in?
**[67:44]** So, I was raised in a Jewish family, and at some point, actually around the time when I was reading Isaac Asimov and Carl Sagan and Richard Dawkins and all the people, around when I was 12 or so, I said,
**[68:05]** This is really all a bunch of Iron Age myths, isn't it?
**[68:12]** None of that was actually true, what
**[68:14]** I had learned about in my Hebrew day school.
**[68:18]** And I became, for a while, a fairly militant atheist, I guess.
**[68:28]** And I thought, OK, the progress of science
**[68:31]** has given less and less room for God, for anything mystical.
**[68:37]** And that's just been the pattern for hundreds of years.
**[68:39]** And there's no reason to expect that that won't continue
**[68:43]** and that God will just get pushed into a tighter
**[68:46]** and tighter corner of maybe setting
**[68:48]** the constants of the standard model of elementary particles.
**[68:52]** But then after that, the walls of physics pretty much
**[68:55]** answer what is going to happen.
**[68:58]** And so that was kind of my view for a while.
**[69:04]** I remember when I was a student, I was in computer science.
**[69:11]** Unfortunately, computer science tends
**[69:13]** to be more than 80% male.
**[69:16]** And I thought, man, if I wanted to meet women,
**[69:25]** the best way would be to go to the Hillel house.
**[69:29]** But then I said, but it would be dishonest for me
**[69:31]** to do that, because I don't really believe in it.
**[69:33]** And then I thought, but it's not really symmetric, is it?
**[69:36]** It's like, OK, if you believe in a personal god who
**[69:39]** really cares about you, then he
**[69:41]** might punish you for going to a secular humanist meetup.
**[69:46]** But there's no atheist god who will
**[69:47]** punish you for going to Hillel.
**[69:50]** If you want to go there and have the social experience,
**[69:52]** then you should just do that.
**[69:54]** And so I sort of evolved to have a more relaxed attitude,
**[69:59]** you could say, where this is just part of whatever
**[70:03]** my history, my culture.
**[70:10]** What does it mean to you to be Jewish?
**[70:13]** Well, it means that, first of all,
**[70:17]** every few generations or so, you know,
**[70:19]** someone is going to try to kill you.
**[70:21]** So you should probably be aware of the rate.
**[70:24]** And like when I was a kid,
**[70:26]** that was just kind of abstract knowledge, right?
**[70:28]** That was like something that I read,
**[70:30]** that I knew because I read it in books
**[70:32]** or because, you know, my grandparents said,
**[70:36]** you know, actually seen it, you know,
**[70:38]** but now, you know, I think we see that
**[70:43]** I think we see that in a much more concrete way.
**[70:45]** So it's first of all, it's that.
**[70:48]** But it's also, you could say, I would
**[70:54]** say I evolved to a position where ethics is really hard.
**[71:01]** We could answer all the questions
**[71:03]** about what elementary particles are going
**[71:10]** to do when you put them in this state or in that state.
**[71:12]** And it still wouldn't answer the questions about, OK,
**[71:15]** how should we live?
**[71:17]** Or which other entities should we even
**[71:23]** regard as having moral value at all?
**[71:26]** Hopefully we regard all other humans as having value.
**[71:29]** What about fetuses?
**[71:34]** What about non-human animals?
**[71:36]** What about AIs?
**[71:38]** Who is in the charm circle of conscious beings
**[71:44]** that we care about?
**[71:45]** And you could say, for all the progress in science,
**[71:48]** there is still this hard problem of consciousness.
**[71:51]** There is still this explanatory gap
**[71:55]** in getting to, well, where do we actually
**[71:59]** enter the picture as agents?
**[72:02]** And so you could set a charitable view toward religion
**[72:09]** would be to say that people have been actually grappling
**[72:11]** with these kinds of things for thousands of years
**[72:14]** with the concepts that were available to them at the time.
**[72:20]** Their science was vastly more primitive than ours was.
**[72:23]** And their morality was also much more primitive
**[72:26]** than ours was, and so they got a lot wrong.
**[72:29]** But if you look at the Buddhist tradition, for example,
**[72:33]** there was a lot of really deep thought there.
**[72:35]** If you look at almost any of the major religious traditions,
**[72:41]** there was a lot of thought there that was worth preserving.
**[72:44]** And I would say the Jewish tradition in particular
**[72:50]** is notable for being maybe one of the first to say,
**[72:56]** Just because, basically, might does not necessarily
**[73:03]** make right.
**[73:07]** When the first temple was destroyed
**[73:10]** and the Jews were exiled to Babylon,
**[73:13]** the normal thing to say, according
**[73:15]** to the Moors of the time, was our god has failed us.
**[73:22]** The true God is the Babylonian God,
**[73:24]** because that's the one who defeated us in war.
**[73:27]** And you could say Judaism, as we know it today,
**[73:32]** started when they said, no.
**[73:34]** We failed God.
**[73:36]** It wasn't that God failed us.
**[73:38]** And you see in the Bible, there is one book
**[73:44]** that deals with these things way more brilliantly
**[73:48]** than anything else, which is Joke, of course, right?
**[73:50]** But they're just sort of directly asking the question
**[73:55]** of how can, if there is this God,
**[74:01]** how can he allow so much injustice
**[74:06]** or cause all of this injustice?
**[74:08]** What's your response to that?
**[74:11]** Well, I don't know.
**[74:12]** I mean, famously, the answer of the book was, well,
**[74:21]** puny human, what makes you think that you could dare
**[74:25]** to try to understand the answer?
**[74:28]** So it's sort of a very unsatisfying non-answer,
**[74:32]** I would say.
**[74:34]** But maybe one answer would be to say, well,
**[74:39]** We shouldn't accept the situation.
**[74:40]** We should fight it.
**[74:42]** And that, the whole project of creating an aligned AI
**[74:47]** is, you could say, it's sort of like people saying,
**[74:50]** well, you know what, screw this.
**[74:54]** If God is going to allow all of this injustice,
**[74:58]** then we should be helping the really just God
**[75:04]** come into being.
**[75:06]** Yeah, I struggled a lot, I thought a lot about going into social politics with you, but I
**[75:13]** found specifically three very interesting thought-provoking blog posts of yours.
**[75:21]** And I just came to the point that I thought, you know, I named this podcast after Frank
**[75:27]** Hill's book, Man's Search for Meaning, and it would have been a disgrace not to
**[75:32]** to talk about what's going on in the world.
**[75:35]** So I would just like to give you the opportunity,
**[75:38]** because I found this blog post about October 7th, right?
**[75:41]** Where you were also advocating to offer refuge
**[75:45]** for Israelis in other lands.
**[75:47]** And yeah, I'd just like to give you the opportunity
**[75:50]** to comment or share your perspective
**[75:52]** about what's happening in Gaza at the moment.
**[75:54]** No, it is, you know, it's a tragedy, you know, that I don't want any innocent people on any
**[76:05]** side to be killed, you know, I've always been a supporter of, you know, what was first
**[76:14]** called partition, what was later called the two-state solution, you know, that has
**[76:19]** always been my end game, you know, to have the different peoples living next to each
**[76:23]** other in peace. And, you know, when I was growing up, so like, you know, when I was
**[76:33]** a teenager, I'd say in the 90s, like that was kind of the liberal position, right?
**[76:39]** That was kind of like an enlightened, like, well-meaning person in the U.S., like
**[76:44]** That was just the obvious thing that you would believe.
**[76:48]** I think that what October 7 laid bare
**[76:51]** is that there's this new, completely different
**[76:54]** understanding that sort of started in academia.
**[76:59]** Well, it started in the Islamic world, in the Soviet Union.
**[77:05]** from there got to academia through people like Edward
**[77:11]** Said.
**[77:12]** And I knew about this ideology because I
**[77:15]** was a grad student in Berkeley.
**[77:18]** I was there during September 11th,
**[77:21]** when the night of September 11th,
**[77:23]** there was a whole vigil where there were people basically
**[77:26]** saying, yeah, the US deserved this.
**[77:29]** And that was what they believed.
**[77:32]** And so I, you know, and, you know, and they,
**[77:36]** like there was like a Holocaust memorial event
**[77:39]** and they took it over with a, you know,
**[77:41]** with a Palestine thing, right?
**[77:43]** And they threw rocks and smashed the windows
**[77:46]** at the Hillel Center.
**[77:47]** I've never heard of that.
**[77:48]** Yeah, this was, I know, this all happened in Berkeley
**[77:50]** in 2002, around the time of the second Intifada, okay?
**[77:55]** And so I knew that like there was this sort of,
**[77:59]** perspective that had come from, let's say, post-colonial theory or post-modernism, deconstructionism,
**[78:08]** this whole, it originated in this left fringe within academia that said, no, we don't
**[78:16]** want two states, we don't want a two-state solution, the Jews are just settler-colonialists.
**[78:26]** they don't belong there, they should go back to Poland, or whatever, and of course many
**[78:34]** of them came from, they ended up in Israel in the 1940s because their families had been
**[78:42]** murdered and there was literally nowhere else on earth that would take them at the
**[78:45]** time, so that's how they got there, but they don't belong there, in fact, maybe
**[78:52]** There never was any Jewish connection to that place at all,
**[78:55]** all the archaeology notwithstanding.
**[78:58]** It's all a myth, and they're just settler colonialists.
**[79:05]** They're just like the French in Algeria,
**[79:10]** or white people in South Africa,
**[79:13]** and they just have no right to be there.
**[79:17]** And so this was sort of a very fringe view
**[79:21]** in the American context for decades.
**[79:26]** Then it was sort of after October 7 that we all saw,
**[79:29]** this is metastasized now.
**[79:31]** This has become a mainstream view.
**[79:34]** The very day of that massacre, we
**[79:37]** saw at every major university people cheering it,
**[79:40]** people saying, finally, the Israelis
**[79:43]** getting what they deserved, or what they deserved apparently is to all be killed in a very horrific
**[79:50]** way.
**[79:51]** Do you have a thesis on why it's the Jewish folk out of all that's been ostracized for
**[80:03]** such a long time?
**[80:04]** There's something really, really deep and really primal here that goes back to the
**[80:08]** beginnings of Western civilization.
**[80:10]** But this is something that's been with us
**[80:13]** for thousands of years.
**[80:16]** I mean, if it hadn't been, then there could never
**[80:20]** have been a Holocaust, for example.
**[80:22]** There could never have been the whole history
**[80:24]** of expulsions before that.
**[80:26]** But we are far afield from my expertise at this point.
**[80:31]** expertise at this point. I am not a scholar of anti-Semitism of Jewish history, but what the
**[80:38]** people who do study it say is that it's really in some sense not about Jews, right? It's about
**[80:46]** like, you know, civilizations that sort of need a way to unite all these sort of disparate
**[80:53]** interests you know behind like you know whatever is is most troubling to that
**[80:59]** society whether it's capitalism or whether it's communism or its
**[81:04]** immigration or its feminism or whatever like there has to be a villain who is
**[81:09]** behind the scenes pulling the strings causing this bad thing that you don't
**[81:14]** like to infect your civilization right and if you just if we can all
**[81:18]** just unite to cast out that that sort of you know malign force then then you know
**[81:25]** this then then we'll have a utopian society right and for whatever reason
**[81:29]** you know Jews were sort of slotted into this role you know 2,000 years ago
**[81:33]** right you know a lot of it was you know came from early Christianity and
**[81:37]** from you know the idea that you know that you know the you know of course
**[81:41]** the the the writers of the New Testament you know were Jews right you
**[81:45]** they were a different faction of Jews,
**[81:48]** arguing against the faction that hadn't supported Jesus.
**[81:55]** But then because of that, the idea became the Jews
**[82:02]** were literally guilty of deicide.
**[82:05]** Instead of maybe getting credit for producing the Son of God,
**[82:11]** They got the blame for turning them over to the Romans.
**[82:17]** So there was that, and then there
**[82:20]** was thousands of years of history
**[82:23]** when Jews were excluded from other occupations.
**[82:26]** And so they ended up doing the things
**[82:28]** that no one else would do, which a lot of times
**[82:30]** was involve trading, involve banking.
**[82:34]** And there's a long history of minorities
**[82:36]** who learn to specialize in those kinds of things,
**[82:39]** who then get vilified for it, right?
**[82:41]** I think like the Parsis in India,
**[82:43]** the Chinese in Malaysia, right?
**[82:47]** There are a lot of other examples of that.
**[82:49]** So then, you know, that got mixed in with it as well.
**[82:52]** You know, but there's a long, long history here.
**[82:55]** Yeah, and your blog post on July 4th,
**[82:59]** you celebrated America's 250th birthday
**[83:03]** and called yourself, you know, thoroughly American after all, and at the same time you wrote about
**[83:08]** those Trump 20-28 campaigns including, you know, focusing on quote-unquote heritage Americans,
**[83:15]** which excludes people like you. What is it like for you to be American nowadays?
**[83:23]** I mean, look, I think that, you know, that we have to say like with, you know, those
**[83:31]** of us who believe this have to say like equally loudly that we love America, we love what
**[83:37]** it stands for.
**[83:38]** I mean, the founding of the United States, right, was one of the most spectacular things
**[83:46]** that ever happened in the whole sorry history of the human species, right, where like for
**[83:51]** the first time ever you have a country that is explicitly founded on like what today we
**[83:56]** could recognize as like reasonable, you know, liberal principles, right, and of course,
**[84:01]** you know, these were very compromised people and they, you know, and they, you know,
**[84:05]** some of them were slaves and so forth, but, you know, they built this self-correcting
**[84:12]** machine you know that was that was you know over the centuries was was actually able able to improve
**[84:18]** itself right and you know this was this was an astounding event if one is going to pledge
**[84:26]** allegiance to anything at all you know one should pledge allegiance to that right and so
**[84:31]** I'm very proud to be an American I'm absolutely disgusted by our current president and by what
**[84:37]** what he represents.
**[84:38]** And I don't even know if we need to belabor that.
**[84:42]** The reasons should be sufficiently obvious to anyone.
**[84:47]** But I feel like fundamentally, this
**[84:51]** is arguably the first president we've ever had who really
**[84:55]** does not believe in the founding
**[84:58]** principles of the country at all.
**[85:00]** If he has made it completely clear that if he could,
**[85:04]** he would just be a dictator, right?
**[85:06]** And, you know, he doesn't try to hide that.
**[85:09]** And, you know, I think there are many of his supporters
**[85:11]** who want that and who love that about him.
**[85:14]** And, you know, and the fact that he was able
**[85:17]** to win two elections despite sort of not hiding
**[85:20]** his authoritarian tendencies is terrifying, right?
**[85:26]** You know, and I can know all of that
**[85:28]** And I can still say, you know, and yet, you know,
**[85:31]** sometimes he will do things that I agree with.
**[85:34]** Sure.
**[85:34]** You know, sometimes, you know,
**[85:37]** the extremists on the other side, you know,
**[85:39]** scare me even more than the extremists on that side.
**[85:42]** Nevertheless, you know,
**[85:43]** it is a terrible situation to be in.
**[85:46]** To have, I would say, in both major parties,
**[85:50]** you know, at this point,
**[85:51]** sort of so little respect for sort of
**[85:54]** the basic principles of the enlightenment, right?
**[85:57]** Of liberalism, of free speech, of democracy,
**[86:03]** of science, of having a shared understanding of reality
**[86:08]** that we would have just taken for granted
**[86:11]** when I was growing up.
**[86:12]** Yeah, you mentioned something really, really interesting
**[86:14]** I keep coming back to, which is a phenomena
**[86:18]** we call ambiguity, tolerance and psychology, right?
**[86:22]** Which describes the ability to hold
**[86:26]** two seemingly paradoxes, right?
**[86:29]** Like, specifically you can be a quote unquote
**[86:35]** conservatist and at the same time be pro-abortion, right?
**[86:40]** For whatever reasons.
**[86:42]** And I see this inability in the mainstream or with the majority of people being one of
**[86:52]** the most fundamental problems of our society because we're stuck in this black and white
**[86:58]** thinking.
**[86:59]** Yeah, it's become harder and harder to have conversations across.
**[87:03]** I even noticed this in a very personal way on my blog.
**[87:07]** When I started my blog in 2005, it was easier to have debates in the comments section than
**[87:14]** it is today.
**[87:15]** What do you think that is?
**[87:17]** Well, I think part of it is that the internet just got more and more polarized.
**[87:23]** Part of it is what happened, I guess in my own career, I became better known,
**[87:29]** which had had some nice effects,
**[87:31]** but it also meant that a lot of trolls and crazies
**[87:35]** got attracted to my blog, right?
**[87:38]** And I did take some controversial public stances
**[87:43]** over the years, right?
**[87:44]** And then, you know, and I feel like,
**[87:49]** part of me feels like, you know,
**[87:50]** if I have this platform and I can say something
**[87:53]** that I really believe in,
**[87:54]** was like, why else did I even become a professor
**[87:57]** in the first place?
**[87:58]** What is tenure for, right?
**[88:00]** If it's not to give me the freedom to say things
**[88:05]** that might get someone else in trouble,
**[88:07]** if they say it right.
**[88:08]** And I feel like I don't want to be a coward, right?
**[88:11]** I want to, like my heroes, like Bertrand Russell
**[88:16]** or whoever, be able to just say what is on my mind.
**[88:21]** you know, defend my beliefs with arguments, you know, listen to other people's arguments,
**[88:29]** you know, be willing to change and all of that stuff.
**[88:34]** So part of me feels that way.
**[88:37]** You know, on the other hand, once you take a public stance for something, it can sort
**[88:41]** of overshadow everything else that you do, right?
**[88:44]** And then even if you don't actually get canceled for what you say, right, which fortunately
**[88:50]** I haven't been, there were some close calls, there were some close calls, but I've not
**[88:58]** been canceled, but it could just take a tremendous amount of time, right, when hundreds of people
**[89:07]** or saying mean things about you online and you feel like the intellectual thing to do
**[89:13]** if someone disagrees with me is to go have a debate with them or have a dialogue with
**[89:18]** them.
**[89:19]** But now we're talking about 500 dialogues with 500 of these people, many of whom are
**[89:24]** not interested in the dialogue at all.
**[89:26]** Or if they are, they'll just do a denial of service attack.
**[89:31]** They will just completely wear you down.
**[89:33]** if you try to have, you know, if you try to have that dialogue with them, right?
**[89:37]** And so, you know, it becomes a lot harder.
**[89:42]** For, if there's one thing you want the people listening to take away from this, what would
**[89:52]** it be?
**[89:53]** What's your message for humanity?
**[89:54]** What's your CTA, your call to action?
**[89:57]** Pay attention to what is happening now in AI. I would say don't believe the people who say it's all a scam, it's all a stochastic parrot, it's all just a fake.
**[90:14]** I feel like that perspective is too cynical for its own good.
**[90:18]** The trouble with AI right now is not that it doesn't work.
**[90:22]** It's that it does work.
**[90:25]** It actually does the things that if you sent them back
**[90:29]** in time 20 years ago or 30 years ago,
**[90:31]** anyone would agree that this is intelligent.
**[90:34]** It is only because we've gotten habituated to it now
**[90:37]** that there's even an argument about is this intelligent
**[90:41]** or not.
**[90:41]** And bringing a new form of intelligence
**[90:45]** into the world is inherently not a safe thing.
**[90:49]** I mean, it's not even a safe thing for those of us
**[90:52]** who were parents, right?
**[90:54]** And there we have a lot more similarity to go on, right?
**[90:58]** And the biological intelligences that were created.
**[91:02]** This is an intelligence that there's never
**[91:05]** been anything quite like in the history of the world.
**[91:08]** And so maybe this will go great, right?
**[91:10]** Maybe we will get it to support human flourishing,
**[91:17]** and it will become like the benevolent god who
**[91:27]** didn't show up in all those cases where
**[91:30]** we might have wanted him.
**[91:32]** But now this one actually will show up,
**[91:35]** And we'll just be able to create this sort of messianic age.
**[91:43]** One can equally well imagine utterly disastrous scenarios.
**[91:46]** But there's this saying people have.
**[91:52]** People used to just dismiss this kind of talk as, OK,
**[91:56]** you're reading too much science fiction.
**[91:59]** And so the saying is, well, you better
**[92:00]** get used to talking about science fiction because now we're living in one.
**[92:06]** To close the loop, circling back to man's search for meaning, what in these times makes
**[92:13]** life meaningful for you?
**[92:15]** Well okay, so what makes life meaningful for me right now is first of all my kids,
**[92:22]** my family, my students, you know, teaching.
**[92:27]** I spent two weeks this summer teaching
**[92:31]** theoretical computer science to 11 and 12 year olds
**[92:33]** at a math camp in Utah.
**[92:36]** I should have attended that.
**[92:37]** Huh?
**[92:38]** I should have attended that.
**[92:38]** Yeah, yeah.
**[92:39]** So my nine year old was also there as a camper.
**[92:43]** And I felt like, you know, even these kids are aware
**[92:48]** of kind of the clouds on the horizon, right?
**[92:50]** They're aware that like all the math that they're learning
**[92:52]** is stuff that AI can now do, you know,
**[92:56]** maybe better than they will ever do it.
**[92:59]** But you know what, you know, they're there to learn.
**[93:01]** They're there to learn math, right?
**[93:02]** And, you know, and they put all their devices away
**[93:06]** and we're just using, you know, using the board,
**[93:09]** using pen and paper.
**[93:11]** And for me, understanding math was always
**[93:15]** a source of meaning in life.
**[93:17]** And seeing this new generation that says,
**[93:20]** the hell with everything, we want to learn math.
**[93:23]** Of course, that also gave me a very strong sense of meaning.
**[93:29]** I would say thinking about science gives me meaning.
**[93:32]** I feel like it'll probably continue to do that,
**[93:35]** even if AI does become better than we are at solving
**[93:39]** all the scientific problems.
**[93:41]** Right now, there's still a few things for us to do.
**[93:43]** But even in a world where AI could just
**[93:48]** do all the math and science better than us,
**[93:50]** I feel like I would still derive some meaning from asking
**[93:54]** the AI questions, trying to understand its answers,
**[93:58]** just trying to, I actually want
**[94:00]** to know the answers to some of these big questions.
**[94:04]** So that's another source of meaning for me.
**[94:07]** Scott, this was beyond mind-bending and thought-provoking.
**[94:13]** First of all, I really admire your courage to speak your mind
**[94:19]** and give a voice to people out there.
**[94:24]** And yeah, just have the guts to write and talk
**[94:27]** about these very juicy, very polarizing topics.
**[94:31]** Thank you.
**[94:32]** No, I mean, you added directions
**[94:33]** that I didn't know you were gonna go,
**[94:35]** but that most podcasters don't, but you know.
**[94:38]** Sure.
**[94:38]** You know what?
**[94:39]** That's why we're here.
**[94:40]** Yeah, exactly.
**[94:41]** Thank you so much for the lectures,
**[94:43]** for all the, really like all the eye-opening learnings
**[94:48]** eye-opening learnings about quantum computing, AI and your personal story.
**[94:56]** That was great. Thank you so much, Lukas.
**[94:58]** Of course. Great.
