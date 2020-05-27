#!/bin/bash

tr  [:graph:]  ' '    < $1 > all.tr


tr "’" ' ' < all.tr > all.tr1

tr  "\012\015\041\042\043\044\045\046\047\050\051\053\054\055\056\057\060\061\062\06<200c><200b>3\064\065\066\067\070\071\073\074\075\076\077\100\101\102\103\104\105\106\107\110\<200c><200b>111\112\113\114\115\116\117\120\121\122\123\124\125\126\127\130\131\132\133\135\1<200c><200b>40\173\174\175" '\n' < all.tr1 > all.tr2

cat all.tr2 | sed -e 's/^[ \t]*//' | grep -v ^$ > all.tr3


for WORD in `cat all.tr3`
do
    echo $WORD >> words_in_$1
done

python3 make_unique_words.py words_in_$1

sort unique_words_in_$1 > unique_sorted_words_in_$1

rm all*

rm unique_words_in_$1
