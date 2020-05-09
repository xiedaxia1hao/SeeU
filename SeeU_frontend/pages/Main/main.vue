<template>
	<view class="main">
		<wuc-tab :tab-list="tabList" :tabCur.sync="TabCur" @change="tabChange" tabClass="tab" textFlex tabStyle="background-color: white;"></wuc-tab>
		
		<!-- Moments Page -->
		<div class="momentPage" v-if="TabCur== 0">
			
			<div class="headline">
				<div>
					<div>Moments</div>
					<input type="text" placeholder="Search" placeholder-style="padding: 4px; font-size: 18px; font-weight: 400;">
				</div>
				<!-- <uni-icons type="contact" size="30"></uni-icons> -->
				
				<div v-for="(moment, index) in momentList">
					<div class="moment">
						<div class="left">
							<div class="personalInfo">
								<div><img class="avatar" :src = "moment.avatar"></div>
								<div class="name">{{moment.name}}</div>
							</div>
							<div class="timeBox">
								<div class="time">{{moment.postTime}}</div>
								<div class="date">{{moment.postDate}}</div>
								<div class="date">{{moment.postYear}}</div>
							</div>
						</div>
						<div class="right">
							<iframe class="player" frameborder="0" src="https://v.qq.com/txp/iframe/player.html?vid=q0892x24nbz" allowFullScreen="true"></iframe>
							<!-- <video src=""></video> -->
						</div>
						
					</div>
				</div>
			</div>
			
			
		</div>
		
		<!-- Publish Page -->
		<div v-if="TabCur== 1">
			
			
		</div>
		
		<!-- Me Page -->
		<div v-if="TabCur== 2">
			
		</div>
		
	</view>
</template>
<script>
import WucTab from '@/components/wuc-tab/wuc-tab.vue';
import uniIcons from "@/components/uni-icons/uni-icons.vue"

	export default {
		data() {
			return {
				TabCur: 0,
				tabList: [{ name: 'Moments', icon: 'cuIcon-comment' }, { name: 'Publish' }, { name: 'Me'}],
				momentList: [
					{
						name: 'Jack',
						avatar: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589018623146&di=1b5e57c864ac277c937bfe856c65ab05&imgtype=0&src=http%3A%2F%2Fimg.mp.itc.cn%2Fupload%2F20170504%2F2a96413cccc64312a6329aed2e588b95_th.jpg',
						postYear: '2020',
						postDate: 'Jan 6',
						postTime: '08:05',
						videoLink: 'www.baidu.com'
					},
					{
						name: 'Amy',
						avatar: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589018623146&di=1b5e57c864ac277c937bfe856c65ab05&imgtype=0&src=http%3A%2F%2Fimg.mp.itc.cn%2Fupload%2F20170504%2F2a96413cccc64312a6329aed2e588b95_th.jpg',
						postYear: '2020',
						postDate: 'Jan 7',
						postTime: '18:27',
						videoLink: 'www.baidu.com'
					},
					{
						name: 'Amy',
						avatar: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589018623146&di=1b5e57c864ac277c937bfe856c65ab05&imgtype=0&src=http%3A%2F%2Fimg.mp.itc.cn%2Fupload%2F20170504%2F2a96413cccc64312a6329aed2e588b95_th.jpg',
						postYear: '2020',
						postDate: 'Jan 5',
						postTime: '18:27',
						videoLink: 'www.baidu.com'
					},
				]
			}
		},
		onLoad() {
	
		},
		components: { WucTab, uniIcons},
		methods: {
			 tabChange(index) { 
			    this.TabCur = index;
			 },
		}
	}
</script>

<style>
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
