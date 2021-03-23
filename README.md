# Notes

This repo contains notes that I collect and maintain. 

I've long wanted a repository like Chris Albon's but never got around to figuring it out how it works.

That's why I want to build it out here, in the open, with copious notes. It took me a long time to get started and hopefully finish this one day so I want to provide as much documentation as possible so I clear the path ahead for others wanting to do the same. 

Code is GPL licensed so do whatever you want with it, a head nod or attribution would be nice :)

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





# Acknowledgements

* [Chris Albon](https://github.com/chrisalbon/notes)
* [Napster In Blue](https://napsterinblue.github.io/notes/)
