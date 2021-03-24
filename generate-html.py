


template = """
    <div class="row">
      <div class="col-sm-12">
        <div class="card">
          <h3 class="category_header">Python</h3>
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
"""

print(template)