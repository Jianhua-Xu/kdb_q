days:("first"; "second"; "third"; "fourth"; "fifth"; "sixth"; "seventh"; "eighth"; "ninth"; "tenth"; "eleventh"; "twelfth")
lines:(
    "On the {day} day of Christmas";
    "My true love sent to me";
    "A partridge in a pear tree";
    "Two turtle doves";
    "Three french hens";
    "Four calling birds";
    "Five golden rings";
    "Six geese a-laying";
    "Seven swans a-swimming";
    "Eight maids a-milking";
    "Nine ladies dancing";
    "Ten lords a-leaping";
    "Eleven pipers piping";
    "Twelve drummers drumming"
 )

res:{r:ssr[;"{day}";days[x[1]-1]] each lines x; if[3<c:count[x];r:@[r;count[x]-1;{"And ", lower(x)}]];r} each (0 1),/: reverse each 2+til each 1+til 12;
res