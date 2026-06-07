function like(slug) {
    const like_element = document.getElementById("like_tag")
    const count_like_element = document.getElementById("count_like_tag")
    $.get(`/article/like/${slug}`).then(response => {
        if (response["liked"]) {
            like_element.className = "fa fa-heart-o"
            count_like_element.innerText = String(Number(count_like_element.innerText) - 1)
        } else {
            like_element.className = "fa fa-heart"
            count_like_element.innerText = String(Number(count_like_element.innerText) + 1)
        }
    })
}
