<template>
    <q-page id="loading">
        <div id="animationWindow"></div>
        <script src='https://cdnjs.cloudflare.com/ajax/libs/bodymovin/4.8.0/bodymovin.min.js'></script>
    </q-page>
</template>

<script>
	var animData = {
		wrapper: document.querySelector('#animationWindow'),
		animType: 'svg',
		loop: true,
		prerender: true,
		autoplay: true,
		path: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/35984/LEGO_loader.json'
	};
	var anim = bodymovin.loadAnimation(animData);
    anim.setSpeed(1.6);
</script>

<style>
	body {
	background-color: #bbbee6;
	overflow: hidden;
	text-align: center;
	}

	body,
	html {
	height: 100%;
	width: 100%;
	margin: 0;
	padding: 0;
	}

	#animationWindow {
	width: 100%;
	height: 100%;
	}
</style>