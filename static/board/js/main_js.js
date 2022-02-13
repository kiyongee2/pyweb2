//이미지 show
let picture = ["../../static/board/images/bg1.jpg", "../../static/board/images/bg2.jpg",
               "../../static/board/images/bg3.jpg"]
let p_idx = 0;

showPicture();

function showPicture() {
    document.querySelector("#pic").src = picture[p_idx];
    p_idx++;
    if(p_idx === picture.length)
        p_idx = 0;
    setTimeout(showPicture, 2000); //콜백 함수
}

//디지털 시계
setInterval(myWatch, 1000);

function myWatch(){
    let date = new Date();
    let now = date.toLocaleTimeString();
    document.getElementById('demo').innerHTML = now;
}