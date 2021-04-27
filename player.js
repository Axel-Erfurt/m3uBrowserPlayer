(function filterlist() {

  var options = {
    valueNames: ["chlist"]
  }

  var listObj = new List("tvlist", options);
}())

var video;
var playlist;
var tracks;
var current;
var win = document.getElementById("top");

initvideo();
function initvideo(){
    current = 0;
    video = $('#myvideo');
    playlist = $('#playlist');
    tracks = playlist.find('li a');
    len = tracks.length - 1;
    //video[0].volume = .90;
    //video[0].play();
    playlist.find('a').click(function(e){
        e.preventDefault();
        link = $(this);
        current = link.parent().index();
       // window.scrollTo(0,0)
        runvideo(link, video[0]);
    });
    video[0].addEventListener('ended',function(e){
        current++;
        if(current == len){
            current = 0;
            link = playlist.find('a')[0];
        }else{
            link = playlist.find('a')[current];
        }
        //window.scrollTo(0,0)
        runvideo($(link),video[0]);
    });
}
// Se cambió esta parte del código para que la función encuentre la segunda URL a través del atributo data-altsrc
function runvideo(link, video){
    $(video).find('#primarysrc').attr('src', link.attr('href'));
    par = link.parent();
    par.addClass('active').siblings().removeClass('active');
    var hls = new Hls();
    var url = link.attr('href')
    hls.loadSource(url);
    hls.attachMedia(video);
    document.title = par.text();
//    window.alert(link.attr('href'));
}
