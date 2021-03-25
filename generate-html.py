import os

content_dir = "./content"
dirs = [x for x in os.listdir(content_dir) if not x.startswith('.')]
out_path = "themes/berbera/layouts/index.html"

BEFORE = """
{{ define "main" }}
<main>

  <div class="homepage">
    <div class="row">
      <div class="col-sm-12">
        <h1>
          <span class="minor_line">Jan Meppe's Notes On</span>
          <br />
          <span class="major_line">Data Science & Machine Learning</span>
          <br />
          <!-- <span class="minor_line">To Scale Myself</span> -->
        </h1>
      </div>
    </div>

    <div class="row">
      <div class="col-sm-12 blurb">
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
          magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
          consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
          est laborum.
        </p>
      </div>
    </div>
"""

AFTER = """
  </div>
</main>
{{ end }}
"""


def generate_template(dir_name):
  """Given dirname generates HTML template to render markdown files in Go template."""

  template = """
    <div class="row">
        <div class="col-sm-12">
            <div class="card">
                <h4 class="card-header">DIR_NAME</h4>
                <div class="card-body">
                    {{ $section := site.GetPage "DIR_NAME" }}
                    {{ range $section.RegularPagesRecursive }}
                    <ul>
                    <li>
                      <a href="{{.Permalink}}">{{.Title}}</a>
                  </li>
                    </ul>
                    {{ end }}
                </div>
            </div>
        </div>
    </div>
  """.replace("DIR_NAME", dir_name)
  return template


with open(out_path, 'w') as f:
  f.write("\n".join([BEFORE] + [generate_template(x) for x in dirs] + [AFTER]))
