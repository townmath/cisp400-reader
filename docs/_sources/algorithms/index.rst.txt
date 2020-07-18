Algorithms
==========

.. toctree::
   :caption: Algorithms
   :maxdepth: 2

   intro.rst
   model.rst
   refactor.rst
   copy.rst

.. activecode:: sql_demo
   :language: sql

   select current_date;
   create table map(a_key varchar(32) primary key, value);

..   :fromcsv: path/to/csv/file
     :mindimensions: mincols, minrows  -- minDimensions:[10,5]
     :maxHeight: 50?
     :colwidths: 10,10,10,10
     :coltitles: "fruit","cost","quantity","price"

     if "====" in self.content:  
      self.options["autograde"] = 'data-autograde="true"'

.. spreadsheet:: sheet_demo
   :mindimensions: 10,5

   fruit,cost,quantity,price
   apple,2.99,12,"=PRODUCT(B2,C2)"
   ,
   ,
   roman,value
   LIV,"=ARABIC(A6)"


a plot

.. plot::
   :include-source: false

   #import numpy as np
   #import matplotlib.pyplot as plt

   x1 = np.linspace(0.0, 5.0)
   x2 = np.linspace(0.0, 2.0)

   y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
   y2 = np.cos(2 * np.pi * x2)

   plt.subplot(2, 1, 1)
   plt.plot(x1, y1, 'o-')
   plt.title('A tale of 2 subplots')

   plt.ylabel('Damped oscillation')

   plt.subplot(2, 1, 2)
   plt.plot(x2, y2, '.-')
   plt.xlabel('time (s)')
   plt.ylabel('Undamped')

   plt.show()

