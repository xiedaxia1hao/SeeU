<template>
	<view class="content">
		<view class="headline">
			Log In
		</view>
		<view class="text">PLEASE LOG IN YOUR ACCOUNT HERE</view>
		
		<view class="signUpRegion">
			<view class="inputArea">
				Your Email:
				<input type="text">
			</view>
			<view class="inputArea">
				Password:
				<input type="text" password="true">
			</view>
			
		</view>
		
		<button type="warn" class="btn">Log In</button>
		
		<view class="text">
			Haven't had an account? &nbsp&nbsp  <span class="hyperlink" @click="changePageToSignUp"> Sign Up!</span>
		</view>
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				title: 'Hello'
			}
		},
		onLoad() {
	
		},
		methods: {
			changePageToSignUp(){
				uni.navigateTo({
				    url: '/pages/index/signUp'
				});
			}
		}
	}
</script>

<style>
	.btn {
		color: white;
		background-color: rgb(7, 26, 78);
		margin-top: 15px;
	}
	.hyperlink {
		color: #007AFF;
		text-decoration: underline;
	}
	input {
		border-bottom: #999999 solid 1px;
	}
	.signUpRegion {
		font-size: 14px;
	}
	
	.inputArea {
		margin-top: 10px;
	}

	.content {
		/* display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		 */
		padding: 20px;
	}
	
	.headline {
		font-size: 30px;
		font-weight: bold;
		text-align: left;
		color: rgb(7, 26, 78);
	}
	
	.text {
		margin-top: 15px;
		margin-bottom: 10px;
		font-size: 14px;
		color: rgb(166, 166, 166);
	}
	
	.logo {
		height: 200rpx;
		width: 200rpx;
		margin-top: 200rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
	}

	.text-area {
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36rpx;
		color: #8f8f94;
	}
</style>
