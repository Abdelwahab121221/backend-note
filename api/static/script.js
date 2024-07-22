let header_update_note = document.querySelectorAll('header ul li')[1]
let header_delete_note = document.querySelectorAll('header ul li')[2]
header_update_note.onclick = function () {
    header_update_note.outerHTML =
    `
    <div>
    <input class = id-field type=text placeholder = 'Enter id'></input>
    <input class = sub-id-field type = button value = 'update'></input>
    </div>
    `
}
header_delete_note.onclick = function () {
    header_delete_note.outerHTML =
    `
    <div>
    <input class = id-field type=text placeholder = 'Enter id'></input>
    <input class = sub-id-field type = button value = 'delete'></input>
    </div>
    `
}
header_update_note.addEventListener('click', () => {
    document.querySelector('.sub-id-field').onclick = function () {
        window.location.href = `/notes/${document.querySelector('header .id-field').value !== null ?document.querySelector('.id-field').value:false}/update`
    }
})
header_delete_note.addEventListener('click', () => {
    document.querySelector('.sub-id-field').onclick = function () {
        window.location.href = `/notes/${document.querySelector('header .id-field').value !== null ?document.querySelector('.id-field').value:false}/delete`
    }
})




update_note = document.querySelectorAll('.content ul li')[1]
delete_note = document.querySelectorAll('.content ul li')[2]
update_note.onclick = function () {
    if (update_note.children[0].tagName === 'A') {
        update_note.innerHTML =
        `
        <input class = id-field type=text placeholder = 'Enter id'></input>
        <input class = sub-id-field type = button value = 'update'></input>
        `
        return false
    }
}
delete_note.onclick = function () {
    if (delete_note.children[0].tagName === 'A') {
        delete_note.innerHTML =
        `
        <input class = id-field type=text placeholder = 'Enter id'>
        <input class = sub-id-field type = button value = 'delete'>
        `
        return false
    }
}
update_note.addEventListener('click', () => {
    document.querySelector('.sub-id-field').onclick = function () {
        window.location.href = `/notes/${document.querySelector('main .id-field').value !== null ?document.querySelector('main .id-field').value:false}/update`
    }
})
delete_note.addEventListener('click', () => {
    document.querySelector('.sub-id-field').onclick = function () {
        window.location.href = `/notes/${document.querySelector('main .id-field').value !== null ?document.querySelector('main .id-field').value:false}/delete`
    }
})
