..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: design patterns; adapter

The Adapter pattern
===================

Design patterns provide a reliable and easy way to follow proven design
principles and to write well-structured and maintainable code.
One of the popular and often used patterns in object-oriented 
software development is the adapter pattern.
It follows Robert C. Martin’s 
`Dependency Inversion Principle <https://en.wikipedia.org/wiki/Dependency_inversion_principle>`__
and enables you to reuse an existing class even so it doesn't implement an
expected interface.

If you do some research on the adapter pattern, you will find two different versions of it:

#. The **class** adapter pattern that implements the adapter using 
   :term:`inheritance <inherit>`.
#. The **object** adapter pattern that uses :term:`composition` 
   to reference an instance of the wrapped class within the adapter.

The object adapter pattern is generally more popular and the one
used within the STL to implement 
:container:`stack` and :container:`queue`.

The general idea of an adapter in software development is identical to the one
in the physical world. 
If you have travelled to foreign countries, 
you probably noticed that electrical outlet vary from country to country.
Outlet shapes vary such that the plug of your electrical device doesn't fit. 
How do you connect the charger of your mobile phone or laptop to these
power outlets?

The answer is simple.
You get an adapter which you can put into the power outlet and 
then you put your plug into the other end of the adapter. 
The adapter changes the form of your plug so that you can use it with 
the power outlet. 
In that example and in most other situations, 
the adapter doesn't provide any additional features.
It just enables you to connect your plug to a different outlet.

Often when programming you have a class that does *almost* what
you need it to, 
or it contains a lot of capability you would like to reuse,
but the class interface is not a good fit.
A class adapter is a simple design pattern that helps solve
problems like this.
We can use an adapter when we want to
convert the interface of a class into another interface clients expect. 
An adapter lets classes work together that couldn't otherwise
because of incompatible interfaces.
An adapter also allows us to 
wrap an existing class with a new interface
without making any changes to the original class - the class being adapted.

The data structures in this chapter :container:`stack` and :container:`queue`
both use the adapter patter to achieve their design goals.

-----

.. admonition:: More to Explore

   - `Sourcemaking - Adapter Design Pattern <https://sourcemaking.com/design_patterns/adapter>`__
   - `DIP in the Wild <https://martinfowler.com/articles/dipInTheWild.html>`__
     (The Dependency Inversion Principle)
   - `Design Patterns Explained - Adapter Pattern with Code Examples <https://stackify.com/design-patterns-explained-adapter-pattern-with-code-examples/>`__

