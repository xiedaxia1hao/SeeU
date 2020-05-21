<template>
	<view class="main">
		<div class="avatarBox">
			<img class="avatarUnderMe" :src = currentPerson.avatar>
			<div>
				<div class="nameUnderMe">{{currentPerson.name}}</div>
				<button class="btn">+ Follow</button>
			</div>
		</div>
		
		<div class="personalHistoryBox">
			<div class="personalHistorySubBox">
				<div class="number">
					{{currentPerson.clipsNum}}
				</div>
				<div class="type">
					Clips
				</div>
			</div>
			
			<div class="personalHistorySubBox">
				<div class="number">
					{{currentPerson.FollowersNum}}
				</div>
				<div class="type">
					Followers
				</div>
			</div>
			
			<div class="personalHistorySubBox">
				<div class="number">
					{{currentPerson.FollowingNum}}
				</div>
				<div class="type">
					Following
				</div>
			</div>
			
		</div>
		
		<div class="SeeUID">SEEU ID: {{SeeUId}}</div>
		<div>
			
			<div class="infoItem">
				Name: 
			</div>
			
			<div class="infoItem">
				WKU Email:
			</div>
			
			<div class="infoItem">
				Contact:
			</div>
		</div>
	</view>
</template>

<script>
	
	export default {
			data() {
				return {
					src: "",
					currentLocation: "",
					currentPerson: {
						name: 'Jack',
						avatar: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589018623146&di=1b5e57c864ac277c937bfe856c65ab05&imgtype=0&src=http%3A%2F%2Fimg.mp.itc.cn%2Fupload%2F20170504%2F2a96413cccc64312a6329aed2e588b95_th.jpg',
						clipsNum: 26,
						FollowersNum: 87,
						FollowingNum: 32
					},
					SeeUId: 7758258,
					TabCur: 0, 
					tabList: [{ name: 'Moments', icon: 'cuIcon-comment' }, { name: 'Publish' }, { name: 'Me'}],
					
				}
			},
			onLoad() {
		
			},
			methods: {
				
			
			}
		}
	
	
</script>

<style>
	
	.infoItem {
		padding: 10px;
		border-bottom: rgb(153, 153, 153) 0.5px dashed;
		font-size: 16px;
	}
	.SeeUID {
		margin-top: 40px;
		font-size: 14px;
		padding: 5px;
		color: rgb(153, 153, 153);
		border-bottom: rgb(153, 153, 153) 1px solid;
	}
	.locationAndMentionBox {
		font-size: 16px;
		margin-top: 30px;
		border-bottom: rgb(153, 153, 153) 1px solid;
		padding: 5px;
	}
	.locationBox {
		overflow: hidden;
		white-space: nowrap;
		text-overflow: ellipsis;
	}
	.photoButton {
		font-size: 50px;
		font-weight: 800;
		height: 130px;
		width: 130px;
		border-radius: 100%;
		background-color: rgb(153, 153, 153);
		color: white;
	}
	.type {
		font-size: 13px;
		font-weight: 400;
		color: #999999;
	}
	.number {
		font-size: 25px;
		font-weight: bold;
	}
	.personalHistorySubBox {
		margin: auto;
		text-align: center;
		width: 32%;
	}
	.personalHistoryBox {
		display: flex;
		justify-content: center;
		height: 80px;
		background-color: rgb(238, 238, 238);
	}
	.avatarUnderMe{
		padding: 10px;
		width: 70px;
		border-radius: 100%;
		height: 70px;
	}
	.avatarBox {
		text-align: left;
		display: flex;
		justify-content: start;
	}
	.nameUnderMe {
		justify-content: center;
		margin-right: 15px;
		padding: 10px;
		font-size: 20px;
		font-weight: bold;
	}
	
	.btn {
		color: white;
		/* height: 30px; */
		background-color: rgb(7, 26, 78);
		font-size: 10px;
	}
	.addClip {
		margin: auto;
	}
	.addClipFont {
		font-size: 14px;
		text-align: center;
		margin-top: 10px;
	}
	.greyArea {
		/* margin-top: 20px; */
		display: flex;
		align-items: center;
		height: 200px;
		background-color: rgb(238, 238, 238);
	}
	.momentPage {
		padding-bottom: 20px;
	}
	.player {
		height: 100%;
		width: 100%;
	}
	.timeBox {
	
		margin-top: 0px;
		margin-left: -30px;
	}
	.date {
		margin-left: 40px;
		font-size: 15px;
		color: black;
		font-weight: 300;
	}
	.time {
		text-align: center;
		font-size: 30px;
		color: black;
		font-weight: 400;
	}
	input {
		background-color: rgb(238, 238, 240);
		height: 35px;
		border-radius: 5px;
	}
	.headline {
		padding: 20px;
		font-size: 30px;
		font-weight: bold;
		text-align: left;
		color: rgb(7, 26, 78);
	}
	.avatar{
		padding: 10px;
		width: 50px;
		border-radius: 100%;
		height: 50px;
	}
	.name {
		padding: 10px;
		margin: auto;
		margin-left: -10px;
		font-size: 20px;
		color: black;
		font-weight: 400;
	}
	
	.personalInfo {
		display: flex;
		justify-content: flex-start;
	}
	.moment {
		display: flex;
		justify-content: flex-start;
		width: 100%;
		margin: 15px 0px 15px 0px;
		background-color: rgb(247, 247, 247);
	}
	
	.left {
		
	}
	
	.right {
		
	}
	
	.main {
		bottom: 100px;
	}
	
	.tab {
		position: fixed;
		bottom: 0;
	}
	
</style>
