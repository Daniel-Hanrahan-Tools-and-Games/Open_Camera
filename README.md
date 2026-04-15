# Open_Camera

A Software solution where anyone can use a homemade digital camera.

If you are going to use this with a Raspberry Pi with ADC then you will need the ADC driver.

If you are going to use this with an Arduino then you will need the Arduino driver.

The software takes a picture by putting all the data in ASCII, grouping all the colors of each pixel into a pixel and all that data is put into a .txt file.

The software does not turn the data into a picture.

The software is configured for 5*5 images.

How to build a homemade digital camera:
What you will need:
<ul>
  <li>box with right size hole for lens and place to add motor</li>
  <li>lens</li>
  <li>motor that is powerful enough to turn a nipkow disc</li>
  <li>dichroic prism</li>
  <li>3 photoresistors</li>
  <li>nipkow disc</li>
</ul>
Steps to build your own homemade digital camera:
<ol>
  <li>Attach lens to lens hole in box using tape or glue.</li>
  <li>Attach motor to place on box for motor.</li>
  <li>Attach dichroic prism behind the lens inside the box</li>
  <li>Attach a photoresistor behind the dichroic prism, that will be your green photoresistor.</li>
  <li>Attach a photoresistor to the left of the dichroic prism, that will be your red or blue photoresistor. To find out if that will be your red or blue photo resistor, aim a white light at your dichroic prism at the opposite side of your green photoresistor.</li>
  <li>Attach a photoresistor to the right of the dichroic prism, that will be your red or blue photoresistor. To find out if that will be your red or blue photo resistor, aim a white light at your dichroic prism at the opposite side of your green photoresistor.</li>
  <li>Do the necessary wiring for each photoresistor.</li>
  <li>Finally attach the nipkow disc through the middle of the disc to the motor and line the holes on the disc with the lens hole.</li>
</ol>

To use mod support you have to put the mod file in Open_Camera folder or later and the mod must be called Open_Camera_Mod.lua

<a href="https://github.com/Daniel-Hanrahan-Tools-and-Games/Open_Camera_Mod">Example Mod Repository Page</a>

<a href="https://github.com/Daniel-Hanrahan-Tools-and-Games/Open_Camera">Repository Page</a>

<a href="https://daniel-hanrahan-tools-and-games.github.io/">Home Page</a>




GNU GPL v3.0 Conditional Exceptions to use MPL 2.0

If the following condition is met, the licensing rules for content covered by GNU GPL v3.0 are modified as described below:

Condition:

The developer is distributing, porting, or integrating the software with platforms or environments that impose requirements incompatible with GPL-3.0, including but not limited to:
- proprietary or non-redistributable SDKs
- confidential hardware or platform documentation
- legally required confidentiality obligations preventing full GPL redistribution
- safety-regulated or certified systems where full GPL redistribution cannot be satisfied

Effect on licensing:

- Content covered by GNU GPL v3.0: May instead be used under the Mozilla Public License 2.0.

These exceptions apply **only when the condition above is met**.





CC BY-SA 4.0 and GNU GPL v3.0 Conditional Exceptions to use PolyForm Noncommercial and CC BY-NC 4.0

The PolyForm Noncommercial License (and Creative Commons
Attribution-NonCommercial 4.0 International for non-code
content) may be used as an alternative only when the combined
work is subject to binding legal, contractual, or platform-
imposed restrictions that prohibit commercial use.

Such restrictions may arise from third-party licenses,
distribution platforms, or other enforceable legal terms that
make commercial use of the combined work not legally permitted.

Content covered by the primary license (e.g., source code or
other covered material) remains governed by that license.

Content not covered by the primary license (e.g., assets,
documentation, or other non-code materials) is governed by
CC BY-NC 4.0, unless otherwise stated.

This alternative applies only to the extent necessary to
comply with such restrictions.




CC BY-SA 4.0 and GNU GPL v3.0 Conditional Exceptions to use PolyForm Strict and CC BY-NC-ND 4.0

The PolyForm Strict License may be used as an alternative
license only when the combined work is subject to binding
legal, contractual, or platform-imposed restrictions that
require both non-commercial use and prohibit the creation of
derivative works as part of the distribution terms.

Such restrictions may arise from third-party licenses,
distribution platforms, or other enforceable legal terms that
impose both non-commercial and no-derivatives requirements on
the combined work.

Content covered by the primary license (e.g., source code or
other covered material) remains governed by that license.

Content not covered by the primary license (e.g., assets,
documentation, or other non-code materials) is governed by
Creative Commons Attribution-NonCommercial-NoDerivatives
4.0 International (CC BY-NC-ND 4.0), unless otherwise stated.

This alternative applies only to the extent necessary to
comply with such restrictions.





contributors needed
