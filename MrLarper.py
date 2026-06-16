import tkinter as tk
from tkinter import ttk, scrolledtext
import random
import base64
import io
import datetime
from PIL import Image, ImageTk, ImageFilter, ImageEnhance

BG_B64 = "/9j/4AAQSkZJRgABAQAAAQABAAD/4gHYSUNDX1BST0ZJTEUAAQEAAAHIAAAAAAQwAABtbnRyUkdCIFhZWiAH4AABAAEAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAAAADTLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlkZXNjAAAA8AAAACRyWFlaAAABFAAAABRnWFlaAAABKAAAABRiWFlaAAABPAAAABR3dHB0AAABUAAAABRyVFJDAAABZAAAAChnVFJDAAABZAAAAChiVFJDAAABZAAAAChjcHJ0AAABjAAAADxtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAAgAAAAcAHMAUgBHAEJYWVogAAAAAAAAb6IAADj1AAADkFhZWiAAAAAAAABimQAAt4UAABjaWFlaIAAAAAAAACSgAAAPhAAAts9YWVogAAAAAAAA9tYAAQAAAADTLXBhcmEAAAAAAAQAAAACZmYAAPKnAAANWQAAE9AAAApbAAAAAAAAAABtbHVjAAAAAAAAAAEAAAAMZW5VUwAAACAAAAAcAEcAbwBvAGcAbABlACAASQBuAGMALgAgADIAMAAxADb/2wBDAAUDBAQEAwUEBAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEPERETFhwXExQaFRERGCEYGh0dHx8fExciJCIeJBweHx7/2wBDAQUFBQcGBw4ICA4eFBEUHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh7/wAARCAEAAQADASIAAhEBAxEB/8QAGwAAAwEBAQEBAAAAAAAAAAAABAUGAwIBBwD/xAA5EAABBAEDAgUCBQMCBQUAAAABAAIDBBEFEiExQQYTIlFhMnEUI0KBoTNSkRViByRDscEWNIKS4f/EABoBAAMBAQEBAAAAAAAAAAAAAAECAwAEBQb/xAAhEQADAQACAgMBAQEAAAAAAAAAAQIRAyESMQQTQTIiUf/aAAwDAQACEQMRAD8A+fSUWuYQ1q4ZVfH1TBrvYLOZ+R0Xs+J8z5aATNDRyk+qWI2RkFNr7sRqT8TTRsgPq5OVPkeHRwLyol9TlY55a3koDC6c7c4uK/Lhvt6ezPSw54X7A7hF1apncBhOaejggPcM/GFtwHlgPoekiV298fXGArrR9L2gekcrjRqTGMDtvAVJp1c/VgAINk7enVSrsOQAfhMo4MjPAW1eHa3hFNg/3fwhpGgaGBwJ56oqKuT+ocfCIirjqBlGR1yPbn4TJaI2BsrEjrldtpv/ALP5TGCHByQiQGf2osm2IJa+Dy0oaSADqm9tv5iFkj46rDS8Fk8Q8s4SyxA5zRg8p7Yj9B4S6aPDViqYkmrFzvUEpv0Qdxx1VNIzKDswb2EBK3g6eEHqVAerjqpTVKpgfuxgL6bqdU+V0Uhr1PdEeEBovsl4nOjfuaSqGG7HIxrnP69R7JAWlp5XcDXvdtYUyY/IUkVlgOGO5RDJ3E9VOthsMOeURBPMw+oK00c1TpQx+bK4NblHVaErmlznZ+MdEhp6m+N4LgmUWt7c9T+6p5o5rloo6VaOIepuT90wDIj9I/lSsetO/tP+VszVn9iQqqkQqKoqq7gWe6/PZ8rKON0LzkZWjpRjkYVn0QF+qM2xOevmvimTdqD2q38WatFXh8sHDsZXza5M6xO6V36iuXnrrD0Ph8b3WDYXTWr83qi4GdumVxnqakO9Cha6u0AZcT1VTWqFzAQQAk+gRMbG0AKroRsLmgjoscvJWUEUq+1jQBwOvynNOEjoMAoeJvGAOiZVhjIAQEdBkURwOQi4mEEdyvIWcDui44njsikK2extDRwUVF3KyEb8dETEx3smEZ2wAuARTG5XEEbd44RLWNHQ4RBgDcibjgDKXWIxtBHCdWYi/og31SeoRwIimbz9kFPF6FQzUjkuxlBzV2gYIwlCnhNywuDuFi6FybWYTvwOEJJwcIZoXyCW3EDlrhwVKazCHOeccFWN7qf3U9fiDtwwthpvs+a24HeYVlBmGTcU61mvsmcQMA8pWyv58oj79kyR0eWoaVsStBR8dOOQYxgpPEZar9p/T/KcaddaZA55yD/CrJDko9OlZ6DH7Ll+mvYM7cqgpuZKfSQQt5W7OwVFGnNXI0TUcEjf0IyGMgHPdPmQQT5eMD4X6ShCW+ng+6PgL9iKCXDhyk2r3YK9cuc7OeiKu2drXMZ7dVD65aHmmMkuJ6KvJWIjEaKdYmltTkuPB7JZJVfj0ptXrusyAN7Im7RdXquc45/Zct6z0+PkSxMmGj1Ae6Nrty8dkIwfnH75TSkz1ZyoNHTT6KXQYyWNwqmi0sAcUk8OxDys+2E/r4DxnogcfI9Y0qjKbU4HO5PCV1pGNZuJwB1KPq6lXDwC7A90UhHTQ9qQkYzymsEe4Zwp2LVqzORJkJlS1ut6fzEUL5MetqsHVbMgjPZBVtWqySBnmt57go+GdjsEYI9wU2BXIjsQNAOOMr1sDVq57NmcrxsjBgo4byRyIV4KzTy5dPssaOAlOs66K0DnMI3DocoJmqs9Bl6GKOPPRSmrXa9d53P6KR8U+ObjN2H525/V/wDi+ca34q1O9kCYjP8ACzQJmqPpWpeIqcTy5r/2SC34mrF+RJhfOGi7ZcGu3yn3W7tH1R3/AEHj90reD/X/ANLaDxFDIdsh3exytbEjJWb43BwK+fvrahWOx0bj7HCK0/UbdZ+CSR3ae62jKEN9crb2Egc4U5pZxqkY+SrB8jLMQc0dQpQt8nXmDbgB2QmQ+9Fk7ToJsBzAQlOoaI+GQvr/AOD0KpqmDEDhFNY2QYIBC6OOFRyVbT7IyhbdVmEczC0qmgkitRelDavogsZfGQD9ko0+axplstkJ25wcqqhySqkx1LHJA7cOR3XrZyRnKbQthvVGva7h38Jfa0+xAS4My33Cb0SQn8SayTI6GlyR9RSvT9MsWJfOsd/dVFDSIYHgmMOI7lNDXBaA0DalctlPs8ViEFelHF9LQsNbgMlB7WgZxlP5q7WjjhLdUZis/wCxU+ScQ8VtI+axtAmPCe6TAJJWtPCTyjFl33KpvCcbZbGXD6QuVrT0qeIqKELIYW7e4RPmhp54XIAAAHZSfiLUHySeRE77lA5t0M17xA8EQ13H0n1HsUq/9R2x7/5WFDS7NuTHO09eOqrNM8JxkNMrQAPdBFVK/SUOvahIcCZw+xWzNU1ENA/Evz919Eb4e06Ngb5TT+y/P0fTmMJMTRj4RwVuV+EJS1TVvxDdtmVv2cr/AMI+KNQaWxSve4j35QrdPpNeHMjb/hGVYq0DgQwBERqWvR9Bo6kbMQw8bkylnLq4LTg9Co/Rpo/M3B3UKlY/0DPcIpkvDDmaeQY5U34hk3Rub7p5qEgjYXZAUV4h1Ha8gOCA0rSU1HTXTSOa8Agoev4eoxvDzGAj33HFxkeRtS+zefIx2ZCyJqDeFkmkOqUGnVRwwAj90TLZqEektH7KOta/FQ2siqtc7+6Tqsodbuai/wD5eOAyHozGMopAcMrnTVT+qMlTutabFJJ58bQM9QAg36s2CUxXaxgkb3AwCjorzbEIAIx7rAxoD01xaTA/qOiS+KAK07Jmj1ZVGyHE3mDBQHier59IHGcFEMvTTQ9UeIWhz8hU9GyJGBwISfR9F8vS2PlaC4j7LBjLETt0YP7FdHFfeEeWNZZQSsIHTKH1jSIbTd4aCSEpqWHOG0ktePfumOnak9kvk2fpPQrpZxtYJdOktaXcMR5j7Aq002wy1XAcGkeyW6vUhtV/NjxuHcILRZpYpvKPGEMB2ODXaFy+MNHHdGtCznHUJ8Iy2K7QxhJ9R5O33Ty2OAEkuxu83jlS5V0dPF3SPnuoM8vUJG56OVN4KaCZHfZIvE9eWGyJXNxlUHgMfkv55XDXR6lPUUMr9sbuM+kqYjr/AIq4e2CqW2HCEgDOUPDE2KIPeMBJukJeBNSOGnXBIGV7Y1xsP1TBg9yVL61qZilLh6nOyGNz1WOn05JoJbU/LnM6d0ZLjez4uq+YWPle/HVaVtThuu3xCZjT3UTUnhpaj+Iu0/xLGggx5I5I4OVT/wDDj8/Usn0QvBJHXCYSkPKsso9MM4lI6hMIJ5Hel2QQsdV02B9xxqzGOX3aMZTPQ6GptkIssbJEW43AclIDoI0uy9kgHwq6vbErQGu5wpSwAxwATbSX8NW0OaHaqXGsSHcqDtwTWbz254BwCru6S+EqLtSGG2/A6FEPil6FOtVGUoC2T+oejUv0inJbm8+YbWNP0nurURVrcImlibI5oxygZqsJk3NYGZ7BAKZ8t1+Yx69NJPC2WKKT0xOPpI9ih9OndLr8VutC2DMoPlsPpaPYL6TqGh6bblMktfc4/KEr6FWqSmWrVaH9iecJgti/xDVdfYS6FoJ7pJShmqvLGk4HurJ9OeUbX7Wj3wh46UYm8vr84QbwXTqvunhDi3PwhdTia6i/PbBTuOv5cZPTH8pdqI4PKyJe2aWrDo9GgY0nLxj/ALIPTZdrgDzhEaRGyxA1juoKVX/Mo3z/AGkq/G8eh5O0UD4IrLBJEQ14X5rYJsxWPQ8cApfRuBxD2H7hMwYrDSSMOC6U9OO0CyNtadIQw+dEeqxGrRbtzWbT903rklvlvw4D3QmpaRHYG+LEcnvjqmE6/SlBXLxzlcQP3epaOPCocqF1r+qVO6pdNSwxzuQSVS2gN5KnNYrskJ3DOOihzdSdnxv6PNWrwapphe1rXFvKX+CmbXTMzna7CawVjFE1u3AwhfDrWR2Zg0Y9RyuGuz079DeV3wl+ox2JBhh9PsEwaNxTWOrG6MHb1StHP6ZGx+HWSSec5xc/5GU3qaY8xhohcnRpSf8ASYiIvxsLNvlNd90Uynl0S58IUJbDZJq8g+x4TvTtF0+h/wC3rhn3R/n3iQBVYu4at6zJh8ZblMLT05iZGJmkNGex9kbJuY0uymFHSWxNL5MFxQ2oRkOcEpkJn5c4lxymmiBznYzwk9iRrJC3qVR+GY2bRwgVXQdLXf5LuFJa/T2ymVowO6+lGofw5ds6qU12rgOaW9UyQ2EpSldHhueM9E0NMTxbmkAnskzvyZy13unml/m8DvjlASkLJaVuN+G8/KGkbqxxtgace5Vwyl/sW8VHI+lZrRFWMgo9I1a00veXM+AUyq6IYWtc/Bd3CtG1XMGA0LKxXIbkYQC3qJWzTa2PBb1UxrsJjyAOOVcX2HafhSniGI4J906EXsU+HmOL3fdMNWoVnua+VuOOSlumT+RaB7Hgpzqjt1fb7lUQbr/Imk0B4cH0Xk554K6jmlrP2WonMI43dinenOLcY4wmzIIp+ZGNcfsuqF0cF2TNa7W38vwmEMzHYIII+EXf8P0rIJDSw/7ThIrnh+5XJdXkLmt6KmE1cscwSlp24yiQcrIhvsvQnIpGNwdUjvN3PxlObfdKLH9RQ5f5Ov4/9HupSFlbI7BK9Bzvlm9z0T50McwaJDjLUt2Rw2pGxnjjK4H0epb6D6xzIFR0x9I9lOVP6oVHSOf8JSWB8ZwU2r145GbtuMoGhDvcHOHHZUFSIFmAAAgkHDCOrCIxhgW7YgBgcD7I2OI7QMrTy2NGS1E3iLnxYGVN+I3mFnp/U7CsZjFtwByoTxRJi81o+kDOPlYMoUMibJYBcFZeHmV2YGcqLt36lSEyzTNYR7oXSPGOnm9tiuMc4dgeqCelfE+/17GnsoYl6qD8WywCWXYcD/wkA8Uh59Uo/wDspPxh4rjjB9W4uz0KoH2MfKbM9znDvwmWhvYyyYT1GML5pR8QXp58NquAd+ojqqrw/ddJqDC09OqAKXR9YpMa6PkI8wtxwcKeoXA2MAlN2Wmludy3oi1jNXs5xlBW27WkLV9tueqX3rI55RCK9SxgqW13BjVFqMjSDg5UtrkmGuHsmQrWEjK8+fuPRpVDNOJKse3skE4DmuOOSjaVyH8KIn5BHCKYhQaY5skeQeqd1jgKX0kt8ve1wd8Kno/0g93dd/D2jz+ZYGMJxyvCN3VexrRoC6Uji1r0IA8HouieF6+Ly25C4e7hROlGVrlqS6jxlN7J9CS6keVLkXR0cPVGtdz5q52H1NGUHE/c9ziPVnlGwf8AL1XvA4IQNNm5zn+/OFwUd9V6GdF35gVJp56/ZSlKTE5GOhCo9Mk/LH2UwplLR+kJ3TfgD2UzUnw0couO03d1WGKd1mNoQ093LCd3RIbWotghJLuqWRX5LEm7PBWC+ikkuZH1ZUh4sjmmZvhG52Oiaefke2PlDTS+6wu49PndrTZbh8mxC4AdigpfBxMofA0sPwV9FmYyVw3dlrBDH/askNXNKISDRNUij2et3zuW0PhiR2JbIDyOg9l9BY1oAAauLDPTkBMT+570Q50gRnbG4MHthM9EowVpg4Ny7uSi7cJ80lYCV0Z44RG+xv2O4rDm4GeFvJdkDdzdxx2CnzbIHLl3DqTWuw7p90rGwewakX8FxB+Vo+wX8kqT1Oy0n8RXdse1O6sjpqTXuxkjnCIGcX7BaCGlT2rP3REnunN7hoU9dduc4JkyTYoYzfkZxhL9Siky1rDjJwnAZtQtwerd1w7KYGnXh989eby3ncCMK00+8NgYSparEyRrJo+M9lQ1a0csOWOw5d/B6OLmWj+vZYRhEtcD0KnhXtMGA7hbRXbEPDmk4XTpwtab5ysLLGA56L9BNlnq4XkpypFE2BWeWpLqpIBcBnCc2XDalGobTuB5yFPk9HVxCyDVHODoN2fZMNO5Y4eyRCo4W9wCf6XyzGFwUdv4dbdthp90/wBNdknHsk08TtwIHKZUHOaMhSfYdGjZpI/pKJhk9X0/ygY5Cc5RVUh0nIQY6oC1KV0t4QHhoHuvz7TYBsY7p3Xd6F0V1zzzubwk2owzB+5pIx7d1jN6M2XnPJDXcreF73u9RJUpDqsEMxBdlzeoRI8QxxtJDh/lEKhsrIYmfVjCKgMDPqfj9lFM8RxvaNry4+wXf+o2rTSyKGXcjoy45/T6BFJXIHraVhftV2AguChrseuVoPOdTsNYSADhZWNJ8QTQRyywSNbINzM9ws2N4caHNzVK2/qP8pfPfrHo8BTs+m6s2U5aQlOotvQbpH52jqfZZsZTH4Vdi7HtLo39Eiuau91gNY0uP3Ux/qFuxL+HgJJPU56K88I+HWNb+Isjc/jBccoJ6akpQXpFK1PCZJeGuGA0q1hqirpscR+oN5X7TqzN0fADR2ROpStwQikQpk5qjyIzg4KQO9TiSU21SQEbfdLasRLi5w+yYi2DPjIbkJdfOWp1cIazCSW8HghMZBehzHG09AeFR1HeUMsPBUZUkdE/IVLpdxksYGeV28L6ObmRXadabK0Nc5bXKbJ+QOUmpgg5acJ1BK7YA7kjuupHnV0yZL9oJAz8LpllpByl9Wyx7Szo4dsruU4bnCj5HV4o6syjbwcpTefkbkVO/LfZLbr/AEkeylddYW412Ctkd5/VOKTiMYKn43/np5SPRcb7Z2L0N6xL35PZGtaGjACDoj1JlAMPykaBpzE714x1R1THmoKRmHbvdaVZA2TCGGTHlqs2eEHAJAS2xVaIyDGcprpkuWkO54Xlhjd5yMpfQ6Z8v8W+E3TwPnoSvjkAz1zn4Ufo0dulqsdbVI3uhJwSei+5WImE8DCSavpFe1GcxNJ78LHRFYTtPU9A0jVTBI5uS0EO6hVXhXxb4Tk1Gw2edkTS0bXPZgHrn/wpSxoMXmZMbf8A5DK0j0Gi8DdA1ENcK5f0t/FPjrwwzSHMgstmceAximZf+KtCxUgrR0bRkhAB+V5V8FUbBBMTRn4TOLwZTghO2GP0/wC3qmRl8SV+kPq3inVrkzvwmn7Yu248/wDZKJKmq3YyLE+Q/wCpuVfXtLiHoDG4HTCxr02j0BgGPhZjfWoEnhzw6yHbiPBPLie6uakIjiawY4CFrMEbMAIqB3KUhy3rHNFzWN3E8johdSlblxXDJQB6kr1KwRkDnKdHLTYttO3yk54C7jZtbgrKL1yDK2sShpLsZTC+xbqTsJPZOCEy1CXOUk1CQbCsVhBOnBkjn98I+mBFMCTnKRaRaLXSZPVPopWTMznBHIXTxVhLlkodNmIcA48KkqOaWD5Udp87RjcU5rWtv0u49l1zR5/JxunqJ/UaZEnmwcOHOEE6y8N2uzlHXLDnRvAI6JLakBdkBQppHVE6byzYGAeUFZlDmHByhrMzmjkoMWtxxuXPdadMcZvCT56fVH42pBB/VBTeq9vHqUCvjhRVJenH8ptXPAcp6rK0AHKbQy+geyJOhg8A44QTsh+QUTE8AZJ6rFwyFmxFQx06wABn7JiHBw65U/VcQ/HZMI5HdEj7KaFyxl3IQjgeQQiYZXY6ZX6Ru8Y6JcwdMCdVEw+kfdeNqxM6gcJjDGWrCeKTJcRwViqtr0cxWGQfTle2dREjNozlB2GlpwVg7hOgffR285wh5S1hyAMlbNie5oOEPOwh2OqxvNs5Ep3AYW7HlvQodrDuBX6d+B6T0SkqN3WA39SDsPEhOChJZiXLpjsgJtOdm4a1vThCXH8LcyfH8oOyeCUTLsVXZTgpHqMx2YxlNdQeGg5SCWTzZD7DhY6+KejTS/qdn3TeKTapmeyK8g7L1ureoAkjPynm8NfE69FjFdw3GTkI2tqDznGTj5UfW1eNn6Cf3RDNZcPoYVWeR/hzv49IcyWy4nAwP+6Dnnb7IRwsuXsVaQjolq9Hnjw5md5vAQW0Nmwmbq/ltyUFajLXh2eAoujpiEFR+lwRkDuQEBL/AEwVpUmHHx8pPI1ThQRH0pjSkcQGk8JPVcMcI+i8B5yn0haH0f8ATGFoB+V0WFWWNwAzlbPdzgdFiLRi+XYQQOfutILBcNzShbQIQbJQwkEIMZFPQsAv9XZMCATkDClqNgh31cJ9WtB4DSeUpRMYwj1hEBjOyWunx0XsU5Jxnql0puhViqw4xwsRRiHLRyjGRkMGV45jD9SdGxALo2Bpw1JbW0ynHCb3ztY4JBZf+aeUWbD0DDSl1yfB254Wtu21keAcJBdtAvOCUqJ0tZt543d/8o6odw57pLSJklOU4r+ghUwk12ElqW3pNpIBR88u2Iu7qe1Gx6zygPEaL9TmBacnKTRPBe4BbXpi47QeqziZtb8nlD0dMLFhhagbK/c5ZN08Sk7eyNLd5AHJTGpFtjAKxXywRjTns6Fax+dC7Lin7K/mds4WslGJ7doatojvQ6KBw6NxlbCEHqf4RbGrZrPdO+jn3BXPXaY+T/CUXIsZHVU8zTs6JJegy/Gevwpt6VihfFh8GChYSY5i0rZgLJsHsVnqIcAJWcYPKBVrRvRl4HKZwOB6KYp2mkDnBTqjOHI6TqR7WlDW4ITBkhOcpEx4cmkUrXH7JjnqQicb2gJPfD4nZzhOYiHfshtUhD2cDqg3ouYLKd0Akbk8p225B3KOtMfVmz2JRlDU43DG5AYtxZjlbjoSj6Ow43cqNpXgTjpn5T2ndDWjc7C2DtliXN8srJ+zjCQ/6qMf1Fi/V/8AemQvkw/Ui3a7lS16RrXnnKJv6kHNd61O6jcZuLg7osFVplqVscpDNZL5CAudRvh25gGSei80SuXcy/sgOkPdFgPDyPsnEhG08dEBXAbEAF7LZIBBKbSTnWc37LfJAaVNahPknlGajaGCAVP25vOcWhBsvEmbGudLknKLc4NhxjosIxtjwVzI/LcJWyyRrXy6UJ3SZnalNBuS3hPqTcbeERKC4GADDR90SxnHVc12gjK3AWItmrGnPRbrFhXW5HdJnsnqwl12EB27P8JiSs5xlhSMaXhK3ovLcXjouY8SN55aR1TS7BvDm4SF/mVpiHfSSgzpl6ga1XkgmdI0+k84Rul3Rwc5CIIbLEM85CV2a768nmx529wgkNSKavbY48FMoJ+AcqMp2wXYJwU3rWiP1BORuG/RUQ2x9P8A5Wrpg8BTsdkh2chH1bYPBRI1DN7tZtiJ3pypjUKNqjIXt+nPYKuY9rx6VxZjbI3a4Aj5WDPRK1NVZt9TuQmMOrAtGJCP3WGqeH45SXw+h3wkFmhdrybWtcflEr46VY1TI/qFZu1TH/UUt5d9v6Hn914YtRfw2Jx/dDTLjQ/uasPKPqSO3qLpZfKYSXFejSNQnYC4hvxnKd6bpkVeMF4DpO5KyYWkhZp2mzSu8yXgdsp7DA2NoAA4W/DW4A4QstkBxAQF1hHm7OMJdqNwDOFnZt7WnlI71kvcQCmGmWc3rRcS1pWdaIgbndT0XleLne8fYLdztqX2VUnMnAyhjITIGAdV7anDB0J+y706LzHGTPXogO+kONPbsiDeqcV2/lgpdWaMDCZsPAACY5+RhcBwES0oFrtq1bI3HVYmaB5ByFoJcj5Qe93uto+MoiJGxevwdlZPkaMLSPlufdAJxKxruyRalVe4nhUL8FBXA17QGnKDZaXiJ6NxiaGk5W42yNXdyseXDkHqEtY59eTB6JS6end2kx/qYNp+ENHadAfLlByO6ZxTxyDkhfp6sUrcEAgrN4Yyhth4GHIyC3hw5Sa1p00B3wOLh7IeK1LE7bK0oqhXOltVugBER3QXYJ/ypKtdHGHIuO56uSjojgrGSscM5X57YJQWyNH3U9FdB9O4hEC7j9SwMGza1dhzgFfjHC3o0f4Sw6g4/rWFnUSIz1WAkxpKYsfTj7IKeZjB9XKWvvlzepS+zcJ/UVg+OjSe07PpdlLp7frPJCXTXy08ElCulllJ28n2QbHiM9hdiyXPIDsrmvAHO8x/7LmCIDDnHOey2dIGcLNjpHUpa0dUHPIcLyeccn2WMEUk8u7PCAx3G10rsBOqdcRxgBuFlQrgDOEzjbloCwlP8NqrBwjGN4Q8Q2jotmv+ExBmi8DPlcr8JPhYB6JW5W7ZHe6Ay0d16Jv9yPoAY85cVvG7DQ3CV/iDnutW2OOqAcGL3EIaUZWX4hdPfubgLGMpWjlLbNVj8nGUdJ6WrJ3qBCDRSWIpo31iXjJaF3Xuns79imMkQc0td0S61SaAXx9fZApLGNew2Tg8LSWnBZbhzQCp6Kd7H7XcJpVv9ASg2FnFnQ3My6BxHwg31rtZxJyQFQwW2uHJRTXNf0wVkBskjPNGQXA4Wgvn2Kp5IIHx7XQsOfhCy6fVc3aImjPsE4MEn+oj3Kzk1AcclOH6LV4xlDy6TXYOQl8jdCiW6ZG4asPzpThgzjqm8lGFgyB0XDpGMbja1o+ENKIBip8h0hB+MLdrIY+RyVzYstAQrrDeywcCnSgHgISSbjGFhJ5kjstKJq1COJSsH0cV6zpnAnp7JrWia2MYC/QxhrQ0FFxgADhFiUawNa1oBOEVGWtCGC/SO24WRNhwkaFnHJ1wgxI73XTH89ERMDfNcvdyEc7heNkz8oi4f//Z"

MODES = ["Rape", "Epstein Mode", "Cloudflare Bypass", "Mr Larp", "Opsex", "Nogger"]

class OpsexDemonV2:
    def __init__(self, root):
        self.root = root
        self.root.title("Opsec Tool - by MrLarper")
        self.root.geometry("700x920")
        self.root.resizable(False, False)
        self.root.configure(bg="#000000")

        self.target_url = tk.StringVar(value="")
        self.num_requests = tk.StringVar(value="1000000")
        self.mode = tk.StringVar(value="Cloudflare bypass")
        self.proxy_var = tk.BooleanVar(value=True)
        self.progress_val = tk.DoubleVar(value=0.0)
        self.running = False
        self._anim_job = None

        self._load_bg()
        self._build_ui()

    def _load_bg(self):
        try:
            img_data = base64.b64decode(BG_B64)
            img = Image.open(io.BytesIO(img_data))
            img = img.resize((350, 350), Image.LANCZOS)
            img = img.filter(ImageFilter.GaussianBlur(radius=1))
            e = ImageEnhance.Brightness(img)
            img = e.enhance(0.55)
            e2 = ImageEnhance.Color(img)
            img = e2.enhance(0.25)
            self.bg_photo = ImageTk.PhotoImage(img)
        except Exception as ex:
            print(ex)
            self.bg_photo = None

    def _lbl(self, parent, text, size=9, color="#ff0000", bold=False, bg="#000000"):
        font = ("Courier New", size, "bold" if bold else "normal")
        return tk.Label(parent, text=text, font=font, fg=color, bg=bg)

    def _entry(self, parent, var, ph=""):
        f = tk.Frame(parent, bg="#1a0000", highlightbackground="#cc0000", highlightthickness=1)
        e = tk.Entry(f, textvariable=var, bg="#000000", fg="#cc3333", insertbackground="#ff0000",
                     font=("Courier New", 10), bd=0, relief="flat")
        e.pack(fill="x", padx=4, pady=4)
        if ph and not var.get():
            e.insert(0, ph)
            e.config(fg="#551111")
            def on_focus_in(event, entry=e, placeholder=ph, svar=var):
                if entry.get() == placeholder:
                    entry.delete(0, "end")
                    entry.config(fg="#cc3333")
            def on_focus_out(event, entry=e, placeholder=ph, svar=var):
                if not entry.get():
                    entry.insert(0, placeholder)
                    entry.config(fg="#551111")
                    svar.set("")
            e.bind("<FocusIn>", on_focus_in)
            e.bind("<FocusOut>", on_focus_out)
        return f

    def _build_ui(self):
        title = tk.Label(self.root, text="MR LARPER", font=("Impact", 28, "bold"),
                         fg="#cc0000", bg="#000000")
        title.pack(pady=(18, 0))

        if self.bg_photo:
            img_lbl = tk.Label(self.root, image=self.bg_photo, bg="#000000", bd=0)
            img_lbl.pack(pady=(10, 0))
        else:
            tk.Label(self.root, text="[ DEMON ]", font=("Courier New", 40, "bold"),
                     fg="#cc0000", bg="#000000").pack(pady=30)

        tk.Label(self.root, text="by MrLarper", font=("Courier New", 11), fg="#ffffff",
                 bg="#000000").pack(pady=(6, 10))

        self.log_box = scrolledtext.ScrolledText(
            self.root, bg="#000000", fg="#cc3333", font=("Courier New", 9),
            bd=0, highlightbackground="#cc0000", highlightthickness=1,
            height=4, wrap="word", state="disabled"
        )
        self.log_box.pack(fill="x", padx=12, pady=(0, 6))
        self._log("DDOS Larp Tool Loaded")

        self._lbl(self.root, "TARGET URL:").pack(anchor="w", padx=12, pady=(4, 0))
        self._entry(self.root, self.target_url, "https://pornhub.org").pack(fill="x", padx=12, pady=(2, 4))

        self._lbl(self.root, "NUMBER OF REQUESTS:").pack(anchor="w", padx=12, pady=(4, 0))
        self._entry(self.root, self.num_requests).pack(fill="x", padx=12, pady=(2, 4))

        self._lbl(self.root, "ATTACK MODE:").pack(anchor="w", padx=12, pady=(4, 0))
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Red.TCombobox", fieldbackground="#000000", background="#000000",
                        foreground="#cc3333", selectbackground="#1a0000",
                        selectforeground="#ff4444", arrowcolor="#cc0000")
        cb_frame = tk.Frame(self.root, bg="#1a0000", highlightbackground="#cc0000", highlightthickness=1)
        cb_frame.pack(fill="x", padx=12, pady=(2, 6))
        cb = ttk.Combobox(cb_frame, textvariable=self.mode, values=MODES,
                          style="Red.TCombobox", state="readonly", font=("Courier New", 10))
        cb.pack(fill="x", padx=2, pady=3)

        chk_frame = tk.Frame(self.root, bg="#000000")
        chk_frame.pack(anchor="w", padx=12, pady=(2, 8))
        tk.Checkbutton(chk_frame, text="  AUTO-FETCH PROXIES  (Evade Detection)",
                       variable=self.proxy_var, bg="#000000", fg="#cc0000",
                       selectcolor="#1a0000", activebackground="#000000",
                       activeforeground="#ff4444", font=("Courier New", 9),
                       highlightthickness=0).pack(side="left")

        prog_frame = tk.Frame(self.root, bg="#1a0000", highlightbackground="#cc0000", highlightthickness=1)
        prog_frame.pack(fill="x", padx=12, pady=(0, 6))
        self.prog_canvas = tk.Canvas(prog_frame, bg="#000000", height=22, bd=0, highlightthickness=0)
        self.prog_canvas.pack(fill="x")
        self.prog_bar = self.prog_canvas.create_rectangle(0, 0, 0, 22, fill="#880000", outline="")
        self.prog_text = self.prog_canvas.create_text(338, 11, text="0%", fill="#ff4444",
                                                       font=("Courier New", 9, "bold"))
        self.prog_canvas.bind("<Configure>", self._on_prog_resize)

        btn_run = tk.Button(self.root, text="Attack the Nigger",
                            command=self._unleash,
                            bg="#330000", fg="#ff4444", activebackground="#550000",
                            activeforeground="#ff6666", font=("Courier New", 11, "bold"),
                            relief="flat", cursor="hand2", bd=0)
        btn_run.pack(fill="x", padx=12, pady=(4, 4), ipady=8)

        btn_abort = tk.Button(self.root, text="Kill Myself",
                              command=self._abort,
                              bg="#1a0000", fg="#884444", activebackground="#330000",
                              activeforeground="#ff4444", font=("Courier New", 11, "bold"),
                              relief="flat", cursor="hand2", bd=0)
        btn_abort.pack(fill="x", padx=12, pady=(0, 12), ipady=8)

    def _on_prog_resize(self, event):
        w = event.width
        pct = self.progress_val.get() / 100.0
        self.prog_canvas.coords(self.prog_bar, 0, 0, int(w * pct), 22)
        self.prog_canvas.coords(self.prog_text, w // 2, 11)

    def _log(self, msg):
        self.log_box.configure(state="normal")
        self.log_box.insert("end", f"> {msg}\n")
        self.log_box.see("end")
        self.log_box.configure(state="disabled")

    def _unleash(self):
        if self.running:
            return
        self.running = True
        self.progress_val.set(0)
        self._update_bar(0)
        target = self.target_url.get().strip()
        if not target or target == "https://example.com":
            target = "https://example.com"
        mode = self.mode.get()
        proxies = "ENABLED" if self.proxy_var.get() else "DISABLED"
        self._log(f"INITIALIZING {mode.upper()} PROTOCOL...")
        self._log(f"TARGET: {target}")
        self._log(f"PROXIES: {proxies}")
        self._log(f"PACKETS: {self.num_requests.get()}")
        self._animate_progress(0)

    def _animate_progress(self, pct):
        if not self.running:
            return
        if pct >= 100:
            self.running = False
            self._log("MISSION COMPLETE. TARGET DESTROYED.")
            self._update_bar(100)
            self.prog_canvas.itemconfig(self.prog_text, text="100%")
            return
        speed = random.uniform(0.3, 1.8)
        new_pct = min(100, pct + speed)
        self._update_bar(new_pct)
        self.prog_canvas.itemconfig(self.prog_text, text=f"{int(new_pct)}%")
        if int(new_pct) % 10 == 0 and int(new_pct) != int(pct):
            msgs = [
                f"BYPASSING FIREWALL... [{int(new_pct)}%]",
                f"INJECTING PACKETS... [{int(new_pct)}%]",
                f"ROTATING PROXIES... [{int(new_pct)}%]",
                f"EVADING DETECTION... [{int(new_pct)}%]",
                f"RAPINGG TARGET... [{int(new_pct)}%]",
            ]
            self._log(random.choice(msgs))
        self._anim_job = self.root.after(30, lambda: self._animate_progress(new_pct))

    def _update_bar(self, pct):
        self.progress_val.set(pct)
        try:
            w = self.prog_canvas.winfo_width()
            self.prog_canvas.coords(self.prog_bar, 0, 0, int(w * pct / 100), 22)
        except Exception:
            pass

    def _abort(self):
        if self._anim_job:
            self.root.after_cancel(self._anim_job)
            self._anim_job = None
        self.running = False
        self._update_bar(0)
        self.prog_canvas.itemconfig(self.prog_text, text="0%")
        self._log("MISSION ABORTED. RETREATING...")


if __name__ == "__main__":
    root = tk.Tk()
    app = OpsexDemonV2(root)
    root.mainloop()