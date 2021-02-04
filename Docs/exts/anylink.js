function anylink_file(dummy_element, version, repo, target, repo_relative_path) {
    href =  "anylink://AnyFile?"
    
    if (version != ""){
        href = href + "version=" + version + "&"
    }
    href = href + "repo=" + repo
    href = href + "&target=" + target

    if (window.location.protocol == "file:" && repo_relative_path != ""){
       current_dir = path.dirname(window.location.pathname)
       repo_path = path.join(current_dir, DOCUMENTATION_OPTIONS.URL_ROOT, repo_relative_path)
       if (repo_path.startsWith("/") && repo_path[2] == ":"){
         // This is windows path so strip the leading "/"
         repo_path = repo_path.slice(1)
       }
       href = href + "&repo_path=" + repo_path
    }
    dummy_element.parentElement.href = href

    // Remove the dummy element <img> element that trigger the call to this function
    dummy_element.remove()
}