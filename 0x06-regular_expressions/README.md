# 0x06. Regular expression

A regular expression, commonly called a “regexp”, is a sequence of characters that define a search pattern. It is mainly for use in pattern matching with strings, or string matching (i.e. it operates like a “find and replace” command). While it is a very powerful tool, it is also very dangerous because of its complexity.

One thing you have to be careful with is that different languages use different regexp engines. That means that a regexp in Python, for example, will be interpreted differently in Javascript.

Regular expressions are everywhere and software engineers, no matter their positions, will have to use them during their careers. System administrators and DevOps are the ones using them the most because they are very handy for log parsing.

**Read about regexp:**

- http://www.regular-expressions.info/
- http://www.w3schools.com/jsref/jsref_obj_regexp.asp Play with regexp (or compose them):
- Ruby: http://rubular.com/
- PHP/Javascript/Python: https://regex101.com/

> - More info on [Concept page: Regular Expression | Holberton Intranet](https://intranet.hbtn.io/concepts/29)

## Resources

- [Regular expressions - basics](https://www.slideshare.net/neha_jain/introducing-regular-expressions)
- [Regular expressions - advanced](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
- [Rubular is your best friend](https://rubular.com/)
- [Use a regular expression against a problem: now you have 2 problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
- [Learn Regular Expressions with simple, interactive exercises](https://regexone.com/)

## Requirements

- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- All your Bash script files must be executable
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env ruby`
- All your regex must be built for the Oniguruma library

## Tasks

### 0. Simply matching Holberton
![task0](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/ec65557f0da1fbfbff6659413885e4d4822f5b1d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210222%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210222T160636Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=da642ca033fccd6be160d33230e26b26ee70a3c5f5f2378947b260e1bd483ffd)

Requirements:

- The regular expression must match `Holberton`
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
- File: **[0-simply_match_holberton.rb](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x06-regular_expressions/0-simply_match_holberton.rb)**

*_Example:_*

```sh
sylvain@ubuntu$ ./0-simply_match_holberton.rb Holberton | cat -e
Holberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Holberton School" | cat -e
Holberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Holberton School Holberton" | cat -e
HolbertonHolberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Grace Hopper" | cat -e
$
```

---
### 1. Repetition Token #0 

![task1](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/e7db3c377d46453588fc84f3a975661d142fee91.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210222%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210222T160636Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=21add2da622f62de14ad7f1e4b4618847d1880cbab0ed9449a084105ff91dd1b)
Requirements:

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
- File: **[1-repetition_token_0.rb](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x06-regular_expressions/1-repetition_token_0.rb)**


---
### 2. Repetition Token #1 

![task2](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/c59ff11db195d5cf17d1790a5141ae2f234786d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210222%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210222T160636Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3a11635ac2e45d44758aa8c09f7d137fcc30c51af1b2061e267173e679f83340)
Requirements:

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
- File: **[2-repetition_token_1.rb](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x06-regular_expressions/2-repetition_token_1.rb)**


---
### 3. Repetition Token #2

![task3](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/3b6bf4aeca6a0c2de584e7f5d68d11eef57ce205.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210222%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210222T160636Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=01982d549f5141f3cdf9454525aadf5ef6735cbd8991fcc285639b2527f217b8)
Requirements:

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
- File: **[3-repetition_token_2.rb](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x06-regular_expressions/3-repetition_token_2.rb)**


---
### 4. Repetition Token #3 

![task4](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/f8dbcb9cf5ae569a8645027dc46e81cb372ce28e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210222%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210222T160636Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3766de7afe3524941fec2ce03bcdb6d57aceaefa56d0cead1d16ad24b195fb42)
Requirements:

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
- Your regex should not contain square brackets
- File: **[4-repetition_token_3.rb](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x06-regular_expressions/4-repetition_token_3.rb)**


---
### 5. Not quite HBTN yet
Requirements:

- The regular expression must be exactly matching a string that starts with `h` ends with `n` and can have any single character in between
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
- File: **[5-beginning_and_end.rb](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x06-regular_expressions/5-beginning_and_end.rb)**

*_Example:_*

```sh
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e
h8n$
sylvain@ubuntu$
$
```

---
### 6. Call me maybe 
This task is brought to you by Holberton professional advisor [Neha Jain](https://twitter.com/_nehajain), Senior Software Engineer at LinkedIn.

Requirement:

- The regular expression must match a 10 digit phone number
- File: **[6-phone_number.rb](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x06-regular_expressions/6-phone_number.rb)**

*_Example:_*

```sh
sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
$
sylvain@ubuntu$
```

---
### 7. OMG WHY ARE YOU SHOUTING? 


Requirement:

The regular expression must be only matching: capital letters
- File: **[7-OMG_WHY_ARE_YOU_SHOUTING.rb](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x06-regular_expressions/7-OMG_WHY_ARE_YOU_SHOUTING.rb)**

*_Example:_*

```sh
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
sylvain@ubuntu$
```

---
### 8. Textme ***#advanced***
This exercise was prepared for you by Guillaume Plessis, VP of Infrastructure at TextMe. It is something he uses daily. You can thank Guillaume for his project on [Twitter](https://twitter.com/gui).

For this task, you’ll be taking over Guillaume’s responsibilities: one afternoon, a TextMe VoIP Engineer comes to you and explains she wants to run some statistics on the TextMe app text messages transactions.

Requirements:

- Your script should output: `[SENDER],[RECEIVER],[FLAGS]`
    - The sender phone number or name (including country code if present)
    - The receiver phone number or name (including country code if present)
    - The flags that were used
You can find a [log file here](http://intranet-projects-files.s3.amazonaws.com/holbertonschool-sysadmin_devops/78/text_messages.log).
- File: **[](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x06-regular_expressions/)**

*_Example:_*

```sh
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]'
Google,+16474951758,-1:0:-1:0:-1
$
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-10 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE2] [SVC:] [ACT:] [BINF:] [FID:] [from:+17272713208] [to:+19172319348] [flags:-1:0:-1:0:-1] [msg:136:Orbiting this at a distance of roughly ninety-two million miles is an utterly insignificant little blue green planet whose ape-descended] [udh:0:]'
+17272713208,+19172319348,-1:0:-1:0:-1
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:18572406905] [to:14022180266] [flags:-1:0:-1:-1:-1] [msg:136:Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy lies a small unregarded yellow sun.] [udh:0:]'
18572406905,14022180266,-1:0:-1:-1:-1
$
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:12392190384] [to:19148265919] [flags:-1:0:-1:-1:-1] [msg:99:life forms are so amazingly primitive that they still think digital watches are a pretty neat idea.] [udh:0:]'
12392190384,19148265919,-1:0:-1:-1:-1
$
```

---
### 9. Pass LinkedIn technical interview level0 ***#advanced***
One way to get started in getting a Software Engineering job at LinkedIn is to solve their regex puzzle.

Requirements:

Solve LinkedIn regex puzzle: https://engineering.linkedin.com/puzzle
Provide as an answer file a screenshot of the “Congratulations” screen with the date and time of completion
- File: **[101-passed_linkedin_regex_challenge.jpg](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x06-regular_expressions/101-passed_linkedin_regex_challenge.jpg)**

*_Example:_*

![img_task9](https://assets.holbertonschool.com/media_images/files/000/001/208/thumb_1000/Screen_Shot_2020-02-25_at_12.56.14_PM.png)


---

⌨️ con ❤️ por [dany eduard](https://github.com/dany-eduard) 😊
