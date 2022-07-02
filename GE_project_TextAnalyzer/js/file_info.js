// function getValue(){
//     var novel_data = document.getElementById("novel_list");
//     console.log(novel_data);
// }

function file_info(){
    this.data_value = $("#select_novel_list option:selected").val();
    this.data_title = $("#select_novel_list option:selected").text();


    document.getElementById("p_novel_file_name").innerHTML = "Selected file name: " +  this.data_value;
    document.getElementById("p_novel_name").innerHTML = "Selected novel name: " + this.data_title;

    this.data_content = document.getElementById("input_file").files[0];
    var reader = new FileReader();
    reader.onload = function (e){
        var textarea = document.getElementById("novel_content");
        textarea.value = e.target.result;
    }
    reader.readAsText(this.data_content)
}



    // document.getElementById("novel_content").value = this.allText
