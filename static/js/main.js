/* =================================
 ------------------------------------
	Version: 1.0
 ------------------------------------
 ====================================*/
'use strict';


$(window).on('load', function() {
	/*------------------
		Preloder
	--------------------*/
	$(".loader").fadeOut();
	$("#preloder").delay(400).fadeOut("slow");
});


$(function() {
	/*------------------
		Navigation
	--------------------*/
	$('.nav-switch').on('click', function(event) {
		$(this).toggleClass('active');
		$('.nav-warp').slideToggle(400);
		event.preventDefault();
	});

	$('.marker-glider').on("click", function(e) {
		/*------------------
            Плавный скролинг Home страницы
        --------------------*/
		e.preventDefault();
		let id  = $(this).attr('href');
		let top = $(id).offset().top; // получаем координаты блока
		$('body, html').animate({scrollTop: top}, 1000); // плавно переходим к блоку
	});

	$('.scrollup').click(function() {
		$('body, html').animate({scrollTop: 0}, 1000);
	});

	// при прокрутке окна (window)
	$(window).scroll(function() {
		// если пользователь прокрутил страницу более чем на 500px
		if ($(this).scrollTop() > 500) {
			// то сделать кнопку scrollup видимой
			$('.scrollup').fadeIn();
		}
		// иначе скрыть кнопку scrollup
		else {
			$('.scrollup').fadeOut();
		}
	});

	/*------------------
		Background Set
	--------------------*/
	$('.set-bg').each(function() {
		let bg = $(this).data('setbg');
		$(this).css('background-image', 'url(' + bg + ')');
	});


	/*------------------
		Progress Bar
	--------------------*/
	$('.progress-bar-style').each(function() {
		let progress = $(this).data("progress");
		let bgcolor = $(this).data("bgcolor");
		let prog_width = progress + '%';
		if (progress <= 100) {
			$(this).append('<div class="bar-inner" style="width:' + prog_width + '; background: '+ bgcolor +';"><span>' + prog_width + '</span></div>');
		}
		else {
			$(this).append('<div class="bar-inner" style="width:100%; background: '+ bgcolor +';"><span>100%</span></div>');
		}
	});




	/*------------------
		Testimonials
	--------------------*/
	$('.testimonials-slider').owlCarousel({
		loop: true,
		nav: false,
		dots: true,
		margin: 128,
		center:true,
		items: 1,
		mouseDrag: false,
		animateOut: 'fadeOutRight',
		animateIn: 'fadeInLeft',
		autoplay:true
	});


	/*------------------
		Brands Slider
	--------------------*/
	$('.brands-slider').owlCarousel({
		loop: true,
		nav: false,
		dots: false,
		margin : 40,
		autoplay: true,
		responsive : {
			0 : {
				items: 1,
			},
			480 : {
				items: 2,
			},
			768 : {
				items: 4,
			},
			1200 : {
				items: 5,
			}
		}
	});



	/*------------------
		Popular Services
	--------------------*/
	$('.popular-services-slider').owlCarousel({
		loop: true,
		dots: false,
		margin : 40,
		autoplay: true,
		nav:true,
		navText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
		responsive : {
			0 : {
				items: 1,
			},
			768 : {
				items: 2,
			},
			991: {
				items: 3
			}
		}
	});


	/*------------------
		Accordions
	--------------------*/
	$('.panel-link').on('click', function (e) {
		$('.panel-link').removeClass('active');
		let $this = $(this);
		if (!$this.hasClass('active')) {
			$this.addClass('active');
		}
		e.preventDefault();
	});


	/*------------------
		Circle progress
	--------------------*/
	$('.circle-progress').each(function() {
		let cpvalue = $(this).data("cpvalue");
		let cpcolor = $(this).data("cpcolor");
		let cptitle = $(this).data("cptitle");
		let cpid 	= $(this).data("cpid");

		$(this).append('<div class="'+ cpid +' loader-circle"></div><div class="progress-info"><h2>'+ cpvalue +'%</h2><p>'+ cptitle +'</p></div>');

		if (cpvalue < 100) {

			$('.' + cpid).circleProgress({
				value: '0.' + cpvalue,
				size: 110,
				thickness: 7,
				fill: cpcolor,
				emptyFill: "rgba(0, 0, 0, 0)"
			});
		} else {
			$('.' + cpid).circleProgress({
				value: 1,
				size: 110,
				thickness: 7,
				fill: cpcolor,
				emptyFill: "rgba(0, 0, 0, 0)"
			});
		}

	});


	/*------------------
		Отправка комментариев
	--------------------*/
	// animation of sending
	$(".form [type='submit']").each(function(){
		let text = $(this).text();
		$(this).html("").append("<span>"+ text +"</span>").prepend("<div class='status'><i class='fas fa-circle-notch fa-spin spinner'></i></div>");
	});

	// Реакция на отправки контактной формы
	$(".contact-form .site-btn[type='submit']").on("click", function(e){
		let $button = $(this);
		let $form = $(this).closest("form");
		let path = $(this).closest("form").attr("data-path");
		$form.validate({
			submitHandler: function() {
				$button.addClass("processing");
				$.post(path, $form.serialize(),  function(response) {
					let $form = $button.closest("form");
					if(response === true){
						$form.trigger("reset");
						let div = '<div class="container">Ваше сообщение успешно отправлено</div>';
						$.createModal({
							title:'Обратная связь',
							message: div,
							closeButton:true,
							scrollable:false
						});
						$button.addClass("done").removeClass('processing').
						prop("disabled", true);
						// Пассивный антиспам
						return false;
					}else{
						alert("!");
						// Не отправляется
						$button.addClass("done").removeClass('processing').
						prop("disabled", true);
						// Пассивный антиспам
					}
				});
				return false;
			}
		});
	});

	// Реакция на отправки формы с обсуждением
	$(".comment-form").validate({
		submitHandler: function(form) {
			let $form = $(form);
			let $button = $(form).find('.site-btn');
			let path = $form.attr("data-path");
			$button.addClass("processing");
			$.post(path, $form.serialize(),  function(response) {
				//let $form = $button.closest("form");
				if(response === true){
					$form.trigger("reset");
					let div = '<div class="container">Ваш комментарий отправлен. Он будет виден после модерации.</div>';
					$.createModal({
						title:'Обсуждение статей',
						message: div,
						closeButton:true,
						scrollable:false
					});
					$button.addClass("done").removeClass('processing'); //.prop("disabled", true);
					return false;
				}else{
					let div = '<div class="container">При отправке возникла ошибка.</div>';
					$.createModal({
						title:'Обсуждение статьи',
						message: div,
						closeButton:true,
						scrollable:false
					});
				}
			});
			// Стандартно завершаем после удачной отправки
			let $section = $button.closest("section");
			let $target = $('.form-reply-primary');
			$section.appendTo($target);
			$('.reply-comment').attr("value", "");
			$('.comment-text').show();
			$('.cancel-reply').hide();
			return false;
		}
	});


	// Реакция на нажатие комментирования ответа на сообщение
	$('.link-reply').on("click", function(e){
		let $button = $(this);
		let $div = $button.closest("div");
		let comment_id = $div.attr('id');
		let target_id = '#form-reply-' + comment_id;
		let $target = $(target_id);
		//$target.show();
		$(".section-reply").appendTo($target);
		// answer on comment #
		$('.reply-comment').attr("value", comment_id);
		$('.comment-text').hide();
		$('.cancel-reply').show();
		return false;
	});

	// Реакция на отмену комментирование ответа
	$('.cancel-reply').on("click", function(e){
		let $button = $(this);
		let $section = $button.closest("section");
		let $target = $('.form-reply-primary');
		$section.appendTo($target);
		$('.reply-comment').attr("value", "");
		$('.comment-text').show();
		$('.cancel-reply').hide();
		return false;
	});

	// Отключение видимости дополнительных кнопок
	$('.btn-other').hide();

});