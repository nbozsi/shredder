# shredder

A CLI-utility to turn 1 good picture into 4/16/256/... shitty ones.
[Explanation](https://www.reddit.com/r/interestingasfuck/comments/95akrt/transforming_one_photo_of_a_dog_into_four_with_a/) (and my inspiration).  

**Table of Contents**
   * [Basic Usage](#basic-usage)
   * [Flags🎏](#flags)
      + [Count🔁](#count)
      + [Stripes✂️](#stripes)
      + [Keep↔️](#keeep)
      + [Output📤](#output)
      + [-w](#-w)
   * [Examples](#examples)
      + [Count - 2](#count-2)
         - [Stripes - 200](#stripes---200)
         - [Stripes - 40](#stripes---40)
         - [Stripes - 10](#stripes---10)
      + [Count 4](#count-4)
         - [Stripes - 200](#stripes---200-1)
         - [Stripes - 40](#stripes---40-1)

## Basic Usage
```console
$ py main.py <filename>
```
This will output the new image in the working directory named `<filename>_shredded_2-200.<original extension>`.
## Flags🎏
### Count🔁
Number of "reshreds". Recommended to be even, cause with odd numbers, the result will look like its streched. (It's a feature, not a bug, FOR REAL.)  
**default**: `2`
```console
$ py main.py <filename> --count <int>
```
### Stripes✂️
Number of stripes made from the image, when it's an odd number, the result images will slightly differ in width.
**default**: `200`
```console
$ py main.py <filename> --stripes <int>
```
Use this option twice to make custom aspect ratios, instead of the default squared.  
```console
$ py main.py <filename> --s <int> -s <int>
```
### Keeep↔️
Using this flag, the small rectangles aspect ratio will match the aspect ratio of the original image.
**default**: `<originalfilename>_shredded_<count>-<stripes>.<original extension>`
```console
$ py main.py <filename> --keep
```
### Output📤
Path/name of the output file.  
**default**: `<originalfilename>_shredded_<count>-<stripes>.<original extension>`
```console
$ py main.py <filename> --output <string>
```

### -w
Using this flag, the util will not print warnings, and recommend settings.
```console
$ py main.py <filename> -w
```
## Examples
<p align="center">
  <img src="./examples/port_1.jpg" width=1500>
  The original image
</p>

---

### Count - 2
#### Stripes - 200

```console
$ py main.py <filename>
```

<p align="center">
  <img src="./examples/port_1_shredded_2-200-531.jpg" width=1500>
</p>

#### Stripes - 40

```console
$ py main.py <filename> --stripes 40
```

<p align="center">
  <img src="./examples/port_1_shredded_2-40-106.jpg" width=1500>
</p>

#### Stripes - 10

```console
$ py main.py <filename> -s 10
```

<p align="center">
  <img src="./examples/port_1_shredded_2-10-26.jpg" width=1500>
</p>

#### Stripes - 10 and 4

```console
$ py main.py <filename> -s 10 -s 4
```

<p align="center">
  <img src="./examples/port_1_shredded_2-10-4.jpg" width=1500>
</p>

---

### Count 4
#### Stripes - 200

```console
$ py main.py <filename> --count 4
```

<p align="center">
  <img src="./examples/port_1_shredded_4-200-531.jpg" width=1500>
</p>

#### Stripes - 40

```console
$ py main.py <filename> -c 4 -s 40
```

<p align="center">
  <img src="./examples/port_1_shredded_4-40-106.jpg" width=1500>
</p>

---
