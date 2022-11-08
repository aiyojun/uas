<template>
  <div style="position: absolute; top: 0; bottom: 0; left: 0; right: 0; background: #f5f7fd; margin: 0; padding: 0;
  font-family: Roboto, Helvetica, sans-serif; overflow: hidden; color: #333;">
    <div class="header">
      <div style="width: 100%; height: calc(100% - 1px); border-bottom: 1px solid #ddd;">

      </div>
    </div>

    <div class="navigator" :style="{width: navPageState ? `240px` : `48px`}">


      <div style="width: calc(100% - 1px); height: 100%; border-right: 1px solid #ddd;">
        <div style="width: 100%; height: calc(100% - 48px); overflow-x: hidden; overflow-y: auto;">


<!--          <div style="width: 100%; height: 40px;"></div>-->
<!--          <div style="margin: 10px 0; padding-left: 12px; font-size: 14px; color: #888;">Menu</div>-->

          <ul style="margin: 0 0; padding: 0;">
            <li style="list-style-type: none; margin: 0; padding: 0;">
              <div class="navigator-linkage" @click="enterBlock('dashboard')">
                <div v-if="moduleLocation === 'dashboard'" class="navigator-linkage-selected-state"></div>
                <div class="navigator-linkage-icon">
                  <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" style="width: 24px;" :fill="moduleLocation === 'dashboard' ? `#333` : `#707070`">
                    <path d="M96 480c-9.6 0-19.2-3.2-25.6-12.8-12.8-12.8-9.6-35.2 3.2-44.8l377.6-310.4c35.2-25.6 86.4-25.6 118.4 0l377.6 307.2c12.8 9.6 16 32 3.2 44.8-12.8 12.8-32 16-44.8 3.2L531.2 166.4c-9.6-6.4-28.8-6.4-38.4 0L115.2 473.6c-6.4 6.4-12.8 6.4-19.2 6.4zM816 928H608c-19.2 0-32-12.8-32-32v-150.4c0-22.4-38.4-44.8-67.2-44.8-28.8 0-64 19.2-64 44.8V896c0 19.2-12.8 32-32 32H211.2C163.2 928 128 892.8 128 848V544c0-19.2 12.8-32 32-32s32 12.8 32 32v304c0 9.6 6.4 16 19.2 16H384v-118.4c0-64 67.2-108.8 128-108.8s131.2 44.8 131.2 108.8V864h176c9.6 0 16 0 16-19.2V544c0-19.2 12.8-32 32-32s32 12.8 32 32v304C896 896 864 928 816 928z"></path>
                  </svg>
                </div>
                <div v-if="navPageState" class="navigator-linkage-title" :style="{color: moduleLocation === 'dashboard' ? `#333` : `#707070`}">
                  Dashboard
                </div>
              </div>
            </li>

            <li style="list-style-type: none; margin: 0; padding: 0;">
              <div class="navigator-linkage" @click="enterBlock('security')">
                <div v-if="moduleLocation === 'security'" class="navigator-linkage-selected-state"></div>
                <div class="navigator-linkage-icon">
                  <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" style="width: 24px;" :fill="moduleLocation === 'security' ? `#333` : `#707070`">
                    <path d="M726.4 201.6c-12.8-9.6-28.8-6.4-38.4 0-9.6 9.6-16 25.6-9.6 38.4 6.4 12.8 9.6 28.8 12.8 44.8-86.4-201.6-230.4-246.4-236.8-249.6-9.6-3.2-22.4 0-28.8 6.4-9.6 6.4-12.8 19.2-9.6 28.8 12.8 86.4-25.6 188.8-115.2 310.4-6.4-25.6-16-51.2-32-80-9.6-9.6-22.4-16-35.2-12.8-16 3.2-25.6 12.8-25.6 28.8-3.2 48-25.6 92.8-51.2 140.8-22.4 41.6-44.8 86.4-54.4 134.4-32 153.6 35.2 265.6 224 368 6.4 3.2 9.6 3.2 16 3.2 9.6 0 19.2-6.4 25.6-12.8 9.6-16 6.4-35.2-9.6-44.8l-3.2-3.2c-188.8-105.6-214.4-192-192-297.6 9.6-41.6 28.8-76.8 48-118.4 12.8-19.2 22.4-38.4 28.8-57.6 0 9.6 3.2 22.4 3.2 32 0 12.8 9.6 25.6 22.4 28.8 12.8 3.2 25.6 0 35.2-9.6 112-134.4 172.8-256 179.2-364.8 51.2 32 137.6 108.8 182.4 272 3.2 9.6 9.6 19.2 22.4 22.4 9.6 3.2 22.4 0 28.8-6.4 25.6-22.4 38.4-54.4 41.6-86.4 54.4 67.2 115.2 176 108.8 288-6.4 92.8-57.6 172.8-150.4 243.2 35.2-166.4-32-358.4-179.2-457.6-9.6-6.4-22.4-6.4-32-3.2-9.6 6.4-16 16-16 28.8-3.2 89.6-48 144-89.6 198.4-35.2 44.8-70.4 89.6-76.8 150.4 0 16 12.8 32 28.8 35.2 19.2 3.2 32-12.8 35.2-28.8 3.2-41.6 32-76.8 60.8-115.2 35.2-44.8 76.8-99.2 96-176 115.2 108.8 153.6 300.8 83.2 435.2v3.2c0 3.2 0 3.2-3.2 6.4v12.8c0 3.2 0 3.2 3.2 6.4v3.2l3.2 3.2c0 3.2 3.2 3.2 3.2 6.4 0 0 3.2 3.2 6.4 3.2l3.2 3.2s3.2 0 3.2 3.2h19.2c3.2 0 6.4 0 9.6-3.2 163.2-89.6 252.8-208 259.2-345.6 9.6-214.4-169.6-393.6-204.8-416z"></path>
                  </svg>
                </div>
                <div v-if="navPageState" class="navigator-linkage-title" :style="{color: moduleLocation === 'security' ? `#333` : `#707070`}">
                  Security
                </div>
              </div>
            </li>

            <li style="list-style-type: none; margin: 0; padding: 0;">
              <div class="navigator-linkage" @click="enterBlock('server')">
                <div v-if="moduleLocation === 'server'" class="navigator-linkage-selected-state"></div>
                <div class="navigator-linkage-icon">
                  <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" style="width: 24px;" :fill="moduleLocation === 'server' ? `#333` : `#707070`">
                    <path d="M960.64 256c0-52.928-43.072-96-96-96l-185.6 0c-0.8 0-1.472 0.416-2.272 0.448-3.424 0.224-6.848 0.704-10.08 2.048-0.448 0.192-0.8 0.576-1.248 0.8-3.168 1.472-6.272 3.136-8.928 5.696-16.576 16.032-25.088 47.904-34.528 87.936-1.312 5.536-2.4 10.336-3.52 14.496-1.44 5.76-4.064 16.48-27.264 16.48C588.416 287.904 578.624 288 576 288L160 288c-52.928 0-96 43.072-95.904 98.464L96 800c0 52.928 43.072 96 96 96l640 0c52.928 0 96-43.072 95.904-93.536M864 800c0 17.664-14.336 32-32 32L192 832c-17.632 0-32-14.336-32.096-34.464L128 384c0-17.632 14.368-32 32-32l416 0c2.784 0 12.576-0.096 15.2-0.096 45.92 0 79.328-24.352 89.216-64.512 1.056-4 2.368-9.472 3.872-15.808C686.72 261.216 692.288 237.632 697.056 224l167.584 0c17.664 0 32 14.368 32 32l0 2.272c0 0.128-0.064 0.224-0.064 0.352L864 800z"></path>
                    <path d="M128 224l416 0c17.696 0 32-14.336 32-32s-14.304-32-32-32L128 160C110.336 160 96 174.336 96 192S110.336 224 128 224z"></path>
                  </svg>

                </div>
                <div v-if="navPageState" class="navigator-linkage-title" :style="{color: moduleLocation === 'server' ? `#333` : `#707070`}">
                  Server System
                </div>
              </div>
            </li>

            <li style="list-style-type: none; margin: 0; padding: 0;">
              <div class="navigator-linkage" @click="enterBlock('user')">
                <div v-if="moduleLocation === 'user'" class="navigator-linkage-selected-state"></div>
                <div class="navigator-linkage-icon">
                  <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" style="width: 24px;" :fill="moduleLocation === 'user' ? `#333` : `#707070`">
                    <path d="M796.8 384c0-160-128-288-288-288s-288 128-288 288c0 108.8 57.6 201.6 147.2 249.6-121.6 48-214.4 153.6-240 288-3.2 16 6.4 35.2 25.6 38.4H160c16 0 28.8-9.6 32-25.6 28.8-150.4 160-259.2 313.6-262.4h6.4c156.8 0 284.8-131.2 284.8-288z m-512 0c0-124.8 99.2-224 224-224s224 99.2 224 224c0 121.6-99.2 220.8-220.8 224H502.4c-121.6-6.4-217.6-102.4-217.6-224zM857.6 672c-25.6 0-51.2 9.6-70.4 25.6l-12.8-9.6c-19.2-9.6-38.4-16-60.8-16-57.6 0-102.4 44.8-102.4 99.2 0 35.2 16 54.4 28.8 70.4 0 0 0 3.2 3.2 3.2l102.4 96c12.8 12.8 28.8 19.2 41.6 19.2 16 0 28.8-6.4 41.6-19.2l102.4-99.2c19.2-19.2 32-44.8 32-70.4 0-54.4-48-99.2-105.6-99.2z m28.8 124.8l-99.2 96-99.2-96c-9.6-12.8-12.8-16-12.8-25.6 0-19.2 19.2-35.2 38.4-35.2 9.6 0 16 3.2 22.4 6.4l35.2 22.4c12.8 9.6 28.8 6.4 38.4-3.2l19.2-16c6.4-6.4 16-9.6 28.8-9.6 22.4 0 38.4 16 38.4 35.2 3.2 9.6-3.2 19.2-9.6 25.6z"></path>
                  </svg>
                </div>
                <div v-if="navPageState" class="navigator-linkage-title" :style="{color: moduleLocation === 'user' ? `#333` : `#707070`}">
                  User Manage
                </div>
              </div>
            </li>

            <li style="list-style-type: none; margin: 0; padding: 0;">
              <div class="navigator-linkage" @click="enterBlock('message')">
                <div v-if="moduleLocation === 'message'" class="navigator-linkage-selected-state"></div>
                <div class="navigator-linkage-icon">
                  <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" style="width: 24px;" :fill="moduleLocation === 'message' ? `#333` : `#707070`">
                    <path d="M640 416l-256 0c-17.664 0-32-14.336-32-32s14.336-32 32-32l256 0c17.696 0 32 14.336 32 32S657.696 416 640 416z"></path>
                    <path d="M579.264 544 384 544c-17.664 0-32-14.336-32-32s14.336-32 32-32l195.264 0c17.696 0 32 14.336 32 32S596.928 544 579.264 544z"></path>
                    <path d="M962.24 448c0-211.744-200.96-384-448-384s-448 172.256-448 384c0 116.512 63.04 226.048 172.928 300.672 14.624 9.984 34.528 6.144 44.448-8.512 9.92-14.624 6.112-34.528-8.512-44.448C183.04 633.216 130.24 542.944 130.24 448c0-176.448 172.256-320 384-320 211.744 0 384 143.552 384 320 0 176.448-172.256 320-384 320-1.984 0-3.68 0.768-5.568 1.12-15.136-2.72-30.464 5.216-35.776 20.192-6.144 17.376-46.368 46.656-94.144 73.792 17.44-58.208 9.088-70.688 3.488-78.976-6.72-9.984-17.92-15.936-29.92-15.936-17.664 0-32 14.304-32 32 0 5.824 1.536 11.264 4.256 15.968-3.232 18.208-17.216 60.832-33.056 99.84-4.928 12.096-1.984 25.984 7.392 35.072 6.08 5.888 14.112 8.992 22.272 8.992 4.384 0 8.8-0.896 12.992-2.752 36.48-16.256 147.648-69.12 187.616-125.632C765.344 828.16 962.24 657.568 962.24 448z"></path>
                  </svg>
                </div>
                <div v-if="navPageState" class="navigator-linkage-title" :style="{color: moduleLocation === 'message' ? `#333` : `#707070`}">
                  Message
                </div>
              </div>
            </li>


            <li style="list-style-type: none; margin: 0; padding: 0;">
              <div class="navigator-linkage" @click="enterBlock('assistant')">
                <div v-if="moduleLocation === 'assistant'" class="navigator-linkage-selected-state"></div>
                <div class="navigator-linkage-icon">
                  <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" style="width: 24px;" :fill="moduleLocation === 'assistant' ? `#333` : `#707070`">
                    <path d="M576 988.8l-128 0c-70.592 0-128-57.408-128-128l0-55.68c0-44.512-26.4-112.32-56.48-145.12C260.64 656.8 192 580.704 192 469.696c0-176.448 143.552-320 320-320 176.448 0 320 143.552 320 320 0 111.04-68.64 187.136-71.52 190.304C730.368 692.768 704 760.608 704 805.12l0 55.68C704 931.392 646.592 988.8 576 988.8zM512 213.696c-141.152 0-256 114.848-256 256 0 86.4 54.144 146.464 54.72 147.072 41.088 44.8 73.28 127.552 73.28 188.384l0 55.68c0 35.296 28.704 64 64 64l128 0c35.296 0 64-28.704 64-64l0-55.68c0-60.832 32.192-143.552 73.28-188.384 0.48-0.544 54.72-61.6 54.72-147.072C768 328.544 653.152 213.696 512 213.696z"></path>
                    <path d="M640 576c-13.408 0-25.888-8.48-30.336-21.888l-15.648-46.88-59.36 59.392c-12.512 12.512-32.736 12.512-45.248 0l-59.392-59.392-15.616 46.88c-5.6 16.736-23.68 25.888-40.48 20.224-16.768-5.568-25.824-23.68-20.224-40.48l32-96c3.52-10.528 12.224-18.464 23.008-21.024 10.752-2.56 22.144 0.672 29.984 8.512L512 498.752l73.376-73.376c7.808-7.84 19.168-11.04 29.984-8.512 10.816 2.56 19.488 10.496 23.008 21.024l32 96c5.6 16.768-3.456 34.912-20.224 40.48C646.752 575.456 643.328 576 640 576z"></path>
                    <path d="M863.68 256.32c-8.736 0-17.44-3.552-23.744-10.56-11.84-13.12-10.816-33.344 2.304-45.216l32.512-29.312c13.088-11.84 33.312-10.816 45.184 2.336 11.84 13.12 10.816 33.344-2.304 45.216L885.12 248.064C879.008 253.6 871.328 256.32 863.68 256.32z"></path>
                    <path d="M160.352 256.32c-7.648 0-15.296-2.72-21.408-8.224L106.432 218.752c-13.12-11.84-14.144-32.064-2.336-45.216s32.032-14.176 45.216-2.336l32.512 29.312c13.12 11.84 14.144 32.064 2.336 45.216C177.824 252.736 169.12 256.32 160.352 256.32z"></path>
                    <path d="M512 128c-17.664 0-32-14.336-32-32L480 64c0-17.664 14.336-32 32-32s32 14.336 32 32l0 32C544 113.664 529.664 128 512 128z"></path>
                    <path d="M576 864l-128 0c-17.664 0-32-14.304-32-32s14.336-32 32-32l128 0c17.696 0 32 14.304 32 32S593.696 864 576 864z"></path>
                  </svg>
                </div>
                <div v-if="navPageState" class="navigator-linkage-title" :style="{color: moduleLocation === 'assistant' ? `#333` : `#707070`}">
                  Home Assistant
                </div>
              </div>
            </li>


          </ul>

        </div>


        <div style="width: calc(100% - 20px); margin: 0 10px; height: calc(48px - 1px); line-height: 47px; border-top: 1px solid #ddd;">
          <div v-if="navPageState" style="height: calc(48px - 1px); line-height: 47px; font-size: 12px; color: #707070;">
            <span>Copyright©2022 All rights reserved</span>
<!--            <span>Dai's Blog</span>-->
          </div>
          <div class="central" :style="{transform: navPageState ? `rotate(180deg)` : `rotate(0deg)`}"
               style="position: absolute; right: 12px; bottom: 12px; width: 24px; height: 24px; border-radius: 4px; cursor: pointer; transform: rotateZ(180deg);" @click="navPageState = !navPageState">
<!--            <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" style="width: 24px;" fill="#333">-->
<!--              <path d="M128 514.112c0 21.248 17.216 38.464 38.464 38.464l404.736 0.32-88.064 88.512c-15.04 14.976-15.04 39.36 0 54.4s39.36 14.976 54.4 0l147.712-148.352c2.688-1.536 5.184-3.52 7.488-5.824 7.744-7.744 11.456-17.92 11.264-28.032 0.192-10.112-3.52-20.288-11.264-28.032-2.304-2.24-4.8-4.16-7.488-5.824L537.536 331.264c-15.04-14.976-39.36-14.976-54.4 0-15.04 15.04-15.04 39.424 0 54.464l89.92 90.24L166.464 475.648C145.216 475.648 128 492.864 128 514.112z"></path>
<path d="M213.312 896l597.312 0C857.6 896 896 857.6 896 810.688L896 213.312C896 166.4 857.6 128 810.688 128L213.312 128C165.952 128 128 166.4 128 213.312l0 107.072C128 348.096 146.112 349.632 170.816 358.4c24.64-8.704 42.56-10.176 42.56-37.952L213.376 213.312l597.312 0 0 597.312L213.312 810.624l0-107.136c0-27.712-18.176-29.184-42.816-37.952C145.856 674.368 128 675.776 128 703.552l0 107.136C128 857.6 165.952 896 213.312 896z"></path>-->
<!--            </svg>-->
            <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="#333">
              <path d="M918.4 489.6l-160-160c-12.8-12.8-32-12.8-44.8 0-12.8 12.8-12.8 32 0 44.8l105.6 105.6L512 480c-19.2 0-32 12.8-32 32s12.8 32 32 32l307.2 0-105.6 105.6c-12.8 12.8-12.8 32 0 44.8 6.4 6.4 12.8 9.6 22.4 9.6 9.6 0 16-3.2 22.4-9.6l160-163.2c0 0 0-3.2 3.2-3.2C931.2 518.4 931.2 499.2 918.4 489.6z"></path>
              <path d="M832 736c-19.2 0-32 12.8-32 32l0 64c0 19.2-12.8 32-32 32L224 864c-19.2 0-32-12.8-32-32L192 192c0-19.2 12.8-32 32-32l544 0c19.2 0 32 12.8 32 32l0 64c0 19.2 12.8 32 32 32s32-12.8 32-32L864 192c0-54.4-41.6-96-96-96L224 96C169.6 96 128 137.6 128 192l0 640c0 54.4 41.6 96 96 96l544 0c54.4 0 96-41.6 96-96l0-64C864 748.8 851.2 736 832 736z"></path>
            </svg>
          </div>
<!--          <div style="display: inline-block; width: 14px; height: 14px; position: relative; top: 2px;">-->
<!--            <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" style="width: 100%;" fill="#888">-->
<!--              <path d="M726.4 201.6c-12.8-9.6-28.8-6.4-38.4 0-9.6 9.6-16 25.6-9.6 38.4 6.4 12.8 9.6 28.8 12.8 44.8-86.4-201.6-230.4-246.4-236.8-249.6-9.6-3.2-22.4 0-28.8 6.4-9.6 6.4-12.8 19.2-9.6 28.8 12.8 86.4-25.6 188.8-115.2 310.4-6.4-25.6-16-51.2-32-80-9.6-9.6-22.4-16-35.2-12.8-16 3.2-25.6 12.8-25.6 28.8-3.2 48-25.6 92.8-51.2 140.8-22.4 41.6-44.8 86.4-54.4 134.4-32 153.6 35.2 265.6 224 368 6.4 3.2 9.6 3.2 16 3.2 9.6 0 19.2-6.4 25.6-12.8 9.6-16 6.4-35.2-9.6-44.8l-3.2-3.2c-188.8-105.6-214.4-192-192-297.6 9.6-41.6 28.8-76.8 48-118.4 12.8-19.2 22.4-38.4 28.8-57.6 0 9.6 3.2 22.4 3.2 32 0 12.8 9.6 25.6 22.4 28.8 12.8 3.2 25.6 0 35.2-9.6 112-134.4 172.8-256 179.2-364.8 51.2 32 137.6 108.8 182.4 272 3.2 9.6 9.6 19.2 22.4 22.4 9.6 3.2 22.4 0 28.8-6.4 25.6-22.4 38.4-54.4 41.6-86.4 54.4 67.2 115.2 176 108.8 288-6.4 92.8-57.6 172.8-150.4 243.2 35.2-166.4-32-358.4-179.2-457.6-9.6-6.4-22.4-6.4-32-3.2-9.6 6.4-16 16-16 28.8-3.2 89.6-48 144-89.6 198.4-35.2 44.8-70.4 89.6-76.8 150.4 0 16 12.8 32 28.8 35.2 19.2 3.2 32-12.8 35.2-28.8 3.2-41.6 32-76.8 60.8-115.2 35.2-44.8 76.8-99.2 96-176 115.2 108.8 153.6 300.8 83.2 435.2v3.2c0 3.2 0 3.2-3.2 6.4v12.8c0 3.2 0 3.2 3.2 6.4v3.2l3.2 3.2c0 3.2 3.2 3.2 3.2 6.4 0 0 3.2 3.2 6.4 3.2l3.2 3.2s3.2 0 3.2 3.2h19.2c3.2 0 6.4 0 9.6-3.2 163.2-89.6 252.8-208 259.2-345.6 9.6-214.4-169.6-393.6-204.8-416z"></path>-->
<!--            </svg>-->
<!--          </div>-->
<!--          Author Jun.Dai-->
        </div>
      </div>

    </div>

    <div class="main" :style="{left: navPageState ? `240px` : `48px`, right: `${descPageState ? 300 : 0}px`}">


      <HomePage v-if="moduleLocation === 'dashboard'" />
      <ServerDashboard v-else-if="moduleLocation === 'server'" />

<!--      <div style="margin: 50px;">-->
<!--        <div class="pretty-button" @click="changeDescPageState">description</div>-->
<!--      </div>-->

<!--      <div class="article" style="z-index: 1;">-->
<!--        <h2>Header</h2>-->
<!--        <p>This is first paragraph.</p>-->
<!--      </div>-->

<!--      <div style="width: 100%; min-height: calc(100% - 42px);">-->
<!--      </div>-->
<!--      <div class="central" style="width: 100%; height: 42px; color: #808080; font-size: 12px;">-->
<!--        <span>Copyright © 2022. All rights reserved.</span>-->
<!--      </div>-->

<!--      <div style="margin: 10px; width: calc(100% - 20px); height: calc(100% - 20px - 32px); overflow-y: auto; overflow-x: hidden;">-->
<!--      </div>-->
<!--      -->
<!--      <div style="position: absolute; height: 32px; bottom: 0; left: 0; right: 0; z-index: 2;">-->
<!--        <div style="width: calc(100% - 20px); margin: 0 10px; height: calc(32px - 1px); line-height: 31px; border-top: 1px solid #ddd; text-align: center; font-size: 12px; color: #888;">-->
<!--          Copyright © 2022. All rights reserved.-->
<!--        </div>-->
<!--      </div>-->

    </div>

    <div class="description" :style="{right: `${descPageState ? '0' : '-240px'}`}">
      <div style="width: calc(100% - 1px); height: 100%; border-left: 1px solid #ddd;">

      </div>
    </div>
  </div>
</template>

<script>

import "@/fonts/roboto/roboto.css"
import HomePage from "@/components/HomePage";
import ServerDashboard from "@/components/ServerDashboard";

export default {
  name: "Dashboard",
  components: {ServerDashboard, HomePage},
  data() {
    return {
      navPageState: true,
      descPageState: false,
      moduleLocation: 'dashboard',
    }
  },
  computed: {

  },
  methods: {
    changeDescPageState() {
      this.descPageState = !this.descPageState
    },
    enterBlock(id) {
      this.moduleLocation = id
    }
  }
}
</script>

<style scoped>

.central {
  display: flex;
  justify-content: center;
  align-items: center;
}

.header {
  width: 100%;
  height: 70px;
  z-index: 3;
}

.navigator {
  position: absolute;
  top: 70px;
  left: 0;
  bottom: 0;
  transition: width 0.2s;
  z-index: 2;
  background-color: #fff;
}

.main {
  transition: all 0.2s;
  position: absolute;
  top: 70px;
  /*left: 240px;*/
  bottom: 0;
  z-index: 1;
  overflow-y: auto;
  overflow-x: hidden;
}

.description {
  transition: right 0.3s;
  position: absolute;
  top: 70px;
  bottom: 0;
  width: 240px;
}

.pretty-button {
  display: inline-block;
  height: 32px;
  line-height: 32px;
  padding-left: 16px;
  padding-right: 16px;
  border-radius: 6px;
  background-color: #409eff;
  color: #fff;
  cursor: pointer;
}

.pretty-button:hover {
  background-color: #0079fe;
}

.article {
  margin: 20px 5% 20px 5%;
  width: calc(90% - 40px);
  padding: 5px 20px;
  border-radius: 8px;
  background-color: #fff;
}

.navigator-linkage {
  position: relative;
  padding: 10px 12px;
  display: flex;
  align-items: center;
  cursor: pointer;
}

.navigator-linkage:hover {
  background-color: rgba(23,24,25,0.05);
}
.navigator-linkage-icon {
  width: 24px; height: 24px; border-radius: 4px; margin-right: 10px;
}

.navigator-linkage-title {
  display: inline-block;
  white-space: nowrap;
}

.navigator-linkage-selected-state {
  position: absolute; top: 0; left: 0; bottom: 0; width: 5px;
  /*background: linear-gradient(110deg, #35a5e6, #c850c0);*/
  background-color: #f58f98;
}

</style>