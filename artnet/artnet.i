 %module artnet
 %{
 /* Includes the header in the wrapper code */
 #include "artnet.h"
 %}
        
 /* Parse the header file to generate wrappers */
 %include "artnet.h"
