document.addEventListener('DOMContentLoaded', function() {
    let myIcon = document.querySelectorAll('i');
    let myLink = document.querySelectorAll('.link');
    for (let i = 0; i < myIcon.length; i++){
        myLink[i].addEventListener('click', function(){
            myIcon[i].classList.remove('bi-check-circle');
            myIcon[i].classList.add('bi-check-circle-fill');
            myIcon[i].style.color = '#90EE90';
            alert(myLink[i].getAttribute('title'))
            /*if (i == 0) {
                alert(This)
            }*/

        });
    }
});