**A Bit Of History**

Right where should i begin? Well like many things in life this began on a quiet April eve, when i happened upon the need of a quick wordpress development environment inside a virtual machine. Well as it happened i was using vagrant for most of my projects and decided to find some projects on the world wide interwebs that may satisfy my urge.

Fortunately i found [VVV](https://github.com/Varying-Vagrant-Vagrants/VVV), which is a great project, of that i have no doubt. Unfortunately i found that it installed far more things than i really needed, and also found that it had some bugs, which after a few attempts of trying to initialize the box kept pooping up.

What did i do, in response to this you ask?

I did what any good man would, i gave up, and endeavored to write my own solution using the knowledge and much of the code the people at VVV used, thus it can be said that i would not have been able to create monkey rocket (charming name i know ), without learning from them. 

I did not create a fork, because what we have here is significantly more different that what we have over there.

**What Doth It Do?**

Monkey rocket, should work with a simple ```vagrant up```, and a change to your hosts file, whereupon you add this ```192.168.50.4 local.wordpress.dev```. 

Briskly said you get:

* Ubunutu Precise 32
* nginx
* all the php stuff you need
* mysql
* various tools such as crul, postfix, git, yada yada
* memcached
* wp-cli
* the latest wodpress realease

This should basically set you up with the latest working release of WordPress, accessible to you though local.wordpress.dev, without needing to install it, or do anything for that matter. And thats it you're ready. 

**Credits** 

A big thank you to all of the contributors of [VVV](https://github.com/Varying-Vagrant-Vagrants/VVV), because i used quite a bit of their code, and because its a great project. 