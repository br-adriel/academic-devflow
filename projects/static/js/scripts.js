const filterProjects = () => {

    const buttonFilterProject = document.getElementById('filter_project_button');
    const formFilterProject = document.getElementById('filter_project_form');

    if (buttonFilterProject.classList.contains('disabled')) {
        buttonFilterProject.classList.remove('disabled')
        buttonFilterProject.classList.add('activated')
        formFilterProject.style.display = "block"

    } else if(buttonFilterProject.classList.contains('activated')){
        buttonFilterProject.classList.remove('activated')
        buttonFilterProject.classList.add('disabled')
        formFilterProject.style.display = "none"
    }

}

const check_checkboxes = () => { 
    const get_all_checkboxes = document.querySelectorAll('[name="codigo"]')
    const get_delete_project_button = document.getElementById('delete_project_button')
    const get_edit_project_button = document.getElementById('edit_project_button')
    const get_trash_icon = document.getElementById('trash_icon')
    const get_edit_icon = document.getElementById('edit_icon')

    let cont = 0
    get_all_checkboxes.forEach(element => {
        if(element.checked){
           cont += 1
        }
    }); 
    
    if(cont == 1){
        get_delete_project_button.disabled = false
        get_edit_project_button.disabled = false
        get_trash_icon.style.color = "red"
        get_edit_icon.style.color = "green"
    } else {
        get_delete_project_button.disabled = true
        get_edit_project_button.disabled = true
        get_trash_icon.style.color = "grey"
        get_edit_icon.style.color = "grey"

    }
}

const return_selected_project = () => {
    const get_all_checkboxes = document.querySelectorAll('[name="codigo"]')
    let id = 0
    get_all_checkboxes.forEach(element => {
        if(element.checked){
            id = parseInt(element.id)
        }
    });

    return id
}

const delete_project = () => {
    const project_to_be_deleted = return_selected_project()
    window.location.href = `${project_to_be_deleted}/excluir`

}

const edit_project = () => {
    const project_to_be_edited = return_selected_project()
    window.location.href = `${project_to_be_edited}/editar`

}

const get_filter_project_input = document.getElementById('filter_project_input')
const get_filter_artifact_input = document.getElementById('filter_artifact_input')
get_filter_project_input.onsubmit()
get_filter_artifact_input.onsubmit()
        