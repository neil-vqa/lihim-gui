import{o as e,c as s,a as o,t,b as n,w as l,d as r,v as a,r as i,F as c,e as d,f as u,g as p,h as g,i as h}from"./vendor.41088fa3.js";!function(){const e=document.createElement("link").relList;if(!(e&&e.supports&&e.supports("modulepreload"))){for(const e of document.querySelectorAll('link[rel="modulepreload"]'))s(e);new MutationObserver((e=>{for(const o of e)if("childList"===o.type)for(const e of o.addedNodes)"LINK"===e.tagName&&"modulepreload"===e.rel&&s(e)})).observe(document,{childList:!0,subtree:!0})}function s(e){if(e.ep)return;e.ep=!0;const s=function(e){const s={};return e.integrity&&(s.integrity=e.integrity),e.referrerpolicy&&(s.referrerPolicy=e.referrerpolicy),"use-credentials"===e.crossorigin?s.credentials="include":"anonymous"===e.crossorigin?s.credentials="omit":s.credentials="same-origin",s}(e);fetch(e.href,s)}}();const f={props:{username:String}},w={class:"\n      rounded-full\n      cursor-pointer\n      fill-current\n      text-black\n      hover:text-white\n      hover:bg-black\n    "},m=o("svg",{class:"w-40 h-40",fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",xmlns:"http://www.w3.org/2000/svg"},[o("path",{"stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"1",d:"M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z"})],-1),x={class:"text-3xl text-center pt-5 pb-10"};f.render=function(n,l,r,a,i,c){return e(),s("section",w,[m,o("p",x,t(r.username),1)])};const y=n.create({baseURL:"http://localhost:5000"}),b={props:{username:String},data:()=>({password:null,key:null}),methods:{closeModal(){this.password=null,this.key=null,this.$emit("close")},login(){console.log(this.password),console.log(this.key),y.post("/api/login",{username:this.username,password:this.password,key:this.key}).then((e=>{console.log(e)})).catch((e=>console.log(e)))}}},k={class:"\n      absolute\n      top-0\n      z-10\n      w-full\n      h-full\n      bg-white\n      flex\n      items-center\n      justify-center\n      bg-opacity-95\n    "},v={class:"w-96 space-y-8"},M={class:"text-right"},P=[o("svg",{xmlns:"http://www.w3.org/2000/svg",class:"icon icon-tabler icon-tabler-x",width:"30",height:"30",viewBox:"0 0 24 24","stroke-width":"1.5",stroke:"currentColor",fill:"none","stroke-linecap":"round","stroke-linejoin":"round"},[o("path",{stroke:"none",d:"M0 0h24v24H0z",fill:"none"}),o("line",{x1:"18",y1:"6",x2:"6",y2:"18"}),o("line",{x1:"6",y1:"6",x2:"18",y2:"18"})],-1)],L={class:"bg-white rounded-xl shadow-2xl px-8 py-4 text-center"},S={class:"font-bold text-5xl"},j={class:"bg-white rounded-xl shadow-2xl px-8 py-4"},C={class:"flex flex-col"},U=o("label",{class:"text-xs my-2"},"Password",-1),z=o("label",{class:"text-xs my-2"},"Key File",-1),q=o("button",{type:"submit",class:"\n              bg-gray-500\n              px-3\n              py-3\n              w-full\n              uppercase\n              text-xs text-white\n              rounded-lg\n              hover:bg-gray-900\n            "}," login ",-1);b.render=function(n,i,c,d,u,p){return e(),s("section",k,[o("section",v,[o("div",M,[o("button",{onClick:i[0]||(i[0]=(...e)=>p.closeModal&&p.closeModal(...e)),class:"p-2 rounded-full bg-red-400 text-white"},P)]),o("div",L,[o("h2",S,t(c.username),1)]),o("div",j,[o("form",{onSubmit:i[3]||(i[3]=l(((...e)=>p.login&&p.login(...e)),["prevent"])),class:"space-y-4"},[o("div",C,[U,r(o("input",{type:"password","onUpdate:modelValue":i[1]||(i[1]=e=>u.password=e),class:"bg-gray-100 px-3 py-2 rounded-lg",required:""},null,512),[[a,u.password]]),z,r(o("input",{type:"text","onUpdate:modelValue":i[2]||(i[2]=e=>u.key=e),class:"bg-gray-100 px-3 py-2 rounded-lg",required:""},null,512),[[a,u.key]])]),q],32)])])])};const N={components:{User:f,PasswordModal:b},data:()=>({users:null,togglePasswordModal:!1,userSelected:null}),created(){y.get("/api/users").then((e=>{this.users=e.data.content}))},methods:{openPasswordModal(e){this.userSelected=e,this.togglePasswordModal=!0}}},A={class:"relative w-full h-screen"},B={class:"flex flex-col justify-center items-center w-full"},F=o("div",{class:"flex justify-center"},[o("img",{src:"/static/lihim-logo.29128a64.png",alt:"lihim logo",class:"w-1/2"})],-1),K={class:"flex space-x-5"};N.render=function(t,n,l,a,h,f){const w=i("User"),m=i("PasswordModal");return e(),s("section",A,[o("section",B,[F,o("div",K,[(e(!0),s(c,null,d(h.users,((s,o)=>(e(),g(w,{key:o,username:s,onClick:e=>f.openPasswordModal(s)},null,8,["username","onClick"])))),128))])]),r(p(m,{username:h.userSelected,onClose:n[0]||(n[0]=e=>h.togglePasswordModal=!1)},null,8,["username"]),[[u,h.togglePasswordModal]])])};const V={components:{Login:N}};V.render=function(o,t,n,l,r,a){const c=i("Login");return e(),s("section",null,[p(c)])};h({setup:s=>(s,o)=>(e(),g(V))}).mount("#app");
