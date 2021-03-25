# Notes

This repo contains notes that I collect and maintain. 

I've long wanted a repository like Chris Albon's but never got around to figuring it out how it works.

That's why I want to build it out here, in the open, with copious notes. It took me a long time to get started and hopefully finish this one day so I want to provide as much documentation as possible so I clear the path ahead for others wanting to do the same. 

Code is GPL licensed so do whatever you want with it, a head nod or attribution would be nice :)

## Usage

Put notebooks in `content` folder

Make sure to add this jekyll front matter

```
```

Then run 

```
python make.py && python generate-html.py
```


## Build notes
### 23-01-2020

* To run simply run `hugo server`  
* Structure of the notes is hardcoded in `themes/berbera/layouts/index.html`
    * This is something I want to automate and make modular with Python
* I think I want to remove the navigation bar because I don't need it
* "Layout" of the main page can be found in `themes/berbera/layouts/_default/baseof.html`
* Removed the navbar

```html
<div class="row">
    <div class="col-sm-12">
        <div class="card">
    <h4 class="card-header" id="python_pandas">Pandas</h4>
            <div class="card-body">
                <ul>
                    {{ range (where .Pages "File.Dir" "in" "/python/pandas/").ByTitle }}
                    <li>
                        <a href="{{.Permalink}}">{{.Title}}</a>
                    </li>
                    {{ end }}
                </ul>
            </div>
        </div>
    </div>
</div>
```

We just need to generate some HTML code with the following template?

```html
<div class="row">
    <div class="col-sm-12">
        <div class="card">
    <h4 class="card-header" id="DIRNAME">DIRNAME</h4>
            <div class="card-body">
                <ul>
                    {{ range (where .Pages "File.Dir" "in" "/DIRNAME/").ByTitle }}
                    <li>
                        <a href="{{.Permalink}}">{{.Title}}</a>
                    </li>
                    {{ end }}
                </ul>
            </div>
        </div>
    </div>
</div>
```

## 24-03-2021

* `archetypes/default.md` contains the main `.yaml` frontmatter for each post, edit your own name in there there
* put your notebooks in `content/`
* ideally use lowercase and hyphens for naming
* TODO: change analytics tag
* As far as I am aware now running `make.py` creates the markdown files in the same folder as the ipython notebooks, this is not convenient
* Here's some documentation on Hugo's dir structure https://gohugo.io/getting-started/directory-structure/
    * `content` all content lives in this folder, each top level folder  in hugo is a content section
    * `themes/static` contains static things
    * `themes/layouts` stores templates of how yo

To figure out the structure of how Hugo parses files so I can take the right ones I made a new project with `hugo new server`. Now the thing is that my posts werent appearing. The reason? I had set the value `draft` to `true` and ran `hugo server` which by default doesn't show drafts.

```yaml
---
title: "Post"
date: 2021-03-24T08:07:48+01:00
draft: false
---
```

I think the value `publishDir="docs"` defines where hugo publishes the docs

* googled `iterate over files 1in directory hugo`
* some info on looping https://www.petfactory.se/notes/hugo_notes/

All I have to do is figure out a way how to iterate over the folders

```html
<ul>
    {{ range (where .Pages "File.Dir" "in" "/creating-data/").ByTitle }}
    <li>
    <a href="{{.Permalink}}">{{.Title}}</a>
    </li>
    {{ end }}
</ul>
```

* FUCK YES! I DID IT! I looped over the fucking fiels in the directory. Its not the right one but it is a directory!!!! 

![](/assets/README/2021-03-24-08-56-17.png)

* https://acanalis.github.io/post/concepts-of-hugo/#2-info-for-theme-users

This worked for a bit ... 
```
                        {{ range (readDir "/content/creating-data") }}
                        <li>
                            <p>
                            {{ .Name }}
                            </p>
                        </li>
                        {{ end }}
```


probeersels

```

                    <ul>
                        {{ range (where .Pages "File.Dir" "in" "/machine_learning/basics/") }}
                        <li>
                            <a href="{{.Permalink}}">{{.Title}}</a>
                        </li>
                        {{ end }}
                    </ul>

                    <ul>
                        {{ range (readDir "/content/creating-data") }}
                        <li>
                            <p>
                            {{ .Name }}
                            </p>
                        </li>
                        {{ end }}
                    </ul>

                    {{ range .Pages }} <li>
                    <a href="{{ .Permalink }}">{{ .Title }}</a>
                    </li>
                    {{ end }}

                    ```

Running into this error

```
Failed to render pages: render of "home" failed: "/Users/janmeppe/Documents/Projects/notes/themes/berbera/layouts/index.html:46:39": execute of template failed: template: index.html:46:39: executing "main" at <.Permalink>: can't evaluate field Permalink in type os.FileInfo
```

added `ignoreFIles` to `config.toml`

The problem that I am running into is that my `.Pages` variable is empty.

I changed the content of the `content` folder to look like this 

```
./content
├── advanced
│   ├── post1.md
│   ├── post2.md
│   └── post3.md
├── basics
│   ├── post2.md
│   └── post3.md
└── post1.md
```

And now I ONLY see the post1 ...but that's a whole lot better than before.

```
                    {{range (where .Pages }}
                    <a href="{{ .Permalink }}">{{ .Title }} </a>
                    {{end}}
                    ```

This then works but only shows `post1.md` 

https://stackoverflow.com/questions/53562000/hugo-doesnt-show-pages-in-a-subdirectory-file-dir

Honestly if i sole this problem im gonna cry legit


https://github.com/osmancakir/osmancakirioblog

Guy wit hthe same issue 

https://discourse.gohugo.io/t/posts-not-showing-in-windows-but-showing-in-ubuntu-hugo-server/27971

https://discourse.gohugo.io/t/listing-all-pages-within-sub-directories/31631/2

holy fucking shit is the the solution? 

DONT GET YOUR HOPES UP! 

How the fuck could I have figured out that it wouldve been `RegularPagesRecursive` without anyu fucking hugo knowledge what the fuck 

I feel like I am getting very close. The only thing that is missing is the front matter now. 

It looks like chris albon adds markdown as raw cells to his notebooks

```
      "source": [
        "---\n",
        "title: \"Annotate Nested Function Parameters\"\n",
        "author: \"Chris Albon\"\n",
        "date: 2021-02-19T00:00:00-07:00\n",
        "description: \"How to annotate a function with nested parameters in Python.\"\n",
        "type: technical_note\n",
        "draft: false\n",
        "---"
      ]
    },
    ```

maybe this tool works

https://jekyllnb.readthedocs.io/en/latest/

OK I THINK I FOUND IT. 

The point is that we refer to the `TITLE` variable so we NEED That variable in our front matter. That is the only thing that really matters. Then the links work out.

This front matter works for example

```yaml
title: "advanced 2"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Loading Features From Dictionaries Using Python."
type: technical_note
draft: false
```

https://github.com/earthlab/tutorials/issues/38

LOL This guy ran into EXACTLY the same issue. MOOD. 

> Currently, we're going through all kinds of backflips in the process of
populating yaml frontmatter for notebooks destined to become markdown posts
on our Jekyll site. This is overcomplicated. Instead, let's just include the
yaml in the first cell (markdown) for each notebook.

Some of the notebooks work. Some of the notebooks dont

need to remove the `permalink` in the frontmatter if it doesn't work

This is so freaking weird. Some of the links work but some of the links dont. WHY!? 

## 25-03-2021

What if we add in the yaml file directly? Do the permalinks then work?

OK OK OK OK OK SO it REALLY REALLY needs a front matter.

It really only needs a title, the markdown file

So then for one file it works, but for another one that I Try it DOESNT. WHY NOT?! 

# Acknowledgements

* [Chris Albon](https://github.com/chrisalbon/notes)
* [Napster In Blue](https://napsterinblue.github.io/notes/)
