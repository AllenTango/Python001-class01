-- MySQL dump 10.13  Distrib 8.0.20, for macos10.15 (x86_64)
--
-- Host: 127.0.0.1    Database: douban
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `shorts`
--

DROP TABLE IF EXISTS `shorts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shorts` (
  `movie_id` int NOT NULL AUTO_INCREMENT,
  `name` char(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `type` char(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `show_time` char(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `commits` json DEFAULT NULL,
  PRIMARY KEY (`movie_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shorts`
--

LOCK TABLES `shorts` WRITE;
/*!40000 ALTER TABLE `shorts` DISABLE KEYS */;
INSERT INTO `shorts` VALUES (1,'哪吒之魔童降世','剧情, 喜剧, 动画, 奇幻','2019-07-26','[{\"short_date\": \"2019-07-19\", \"short_star\": \"50\", \"short_title\": \"力荐\", \"short_content\": \"休说苍天不由人，我命由我不由天。新的故事，改编的很不错啊，就是有点短。友情提醒：观影记得带纸巾\"}, {\"short_date\": \"2019-07-19\", \"short_star\": \"40\", \"short_title\": \"推荐\", \"short_content\": \"谢谢把我拍的这么好！\"}, {\"short_date\": \"2019-07-17\", \"short_star\": \"30\", \"short_title\": \"还行\", \"short_content\": \"第一，不觉得好笑；第二，配音出戏；第三，又一部银河补习班。讲完。你们骂吧。\"}, {\"short_date\": \"2019-07-19\", \"short_star\": \"30\", \"short_title\": \"还行\", \"short_content\": \"李靖到底是为了什么做 揭穿敖丙身份 这样损人不利己的事？\"}, {\"short_date\": \"2019-07-17\", \"short_star\": \"20\", \"short_title\": \"较差\", \"short_content\": \"这种段子堆成的对白恕不是我的审美。\"}, {\"short_date\": \"2019-07-21\", \"short_star\": \"30\", \"short_title\": \"还行\", \"short_content\": \"就…大家对国产未免也太宽容…\"}, {\"short_date\": \"2019-07-19\", \"short_star\": \"20\", \"short_title\": \"较差\", \"short_content\": \"各种方言、结巴、放屁、烧裤裆的梗，还有什么指纹解锁、游乐场之类的舔当代科技，所有笑点都能在半分钟之前预知，弱智当好笑。最不能接受的是把主题又变成什么“不信命”之类的俗套，那句泛中国地区最中二病没有之一的“我命由我不由天”出来的时候，我饭都要呕出来，本来我们已经很没有反抗父权的人物了，硕果仅存的哪吒也要变成这样，“削骨还父、割肉还母”完全没有，爹妈爱我，父慈子孝，让人忍不住竖中指，行吧，【父母皆祸害】小组关了，李靖也洗白白了，我服了还不行吗？我信命了好吧\"}, {\"short_date\": \"2019-07-16\", \"short_star\": \"10\", \"short_title\": \"很差\", \"short_content\": \"哪吒这个形象真的是毁童年，很多人都说这部代表着国漫崛起，请问此种好莱坞式的动漫能代表中国文化嘛？\"}, {\"short_date\": \"2019-07-14\", \"short_star\": \"40\", \"short_title\": \"推荐\", \"short_content\": \"点映看完了，不剧透地说，除了哪吒和他娘的人物关系外，这部电影把传统的哪吒故事里人物关系都改变了，哪吒和李靖、哪吒和太乙、哪吒和敖丙等等，因为有这些关系要重新做，所以这些人物的设定才和传统的不一样。整部电影本身严格按照商业片的形式，几个情感转折的节点都掐准了时间，不夸张地说，如果这个系列电影要做下去的话（还有之前的大圣、之后的姜子牙等），《大圣归来》和《魔童降世》在这个系列的地位相当于这个系列的《钢铁侠01》和《美国队长01》，但前提是一定要做下去。\"}, {\"short_date\": \"2019-07-23\", \"short_star\": \"40\", \"short_title\": \"推荐\", \"short_content\": \"承认期待不高，看得有些意外。我不是哪吒迷，而更接近封神迷——实为情怀的那种玩意，所以看到片方想要铺封神宇宙，无论成败，总归是有人在做这么一步，并且，这一步，作为起点是恰如其分的。不存在“哪吒就应该是代表/刻画什么精神”之类的说法，动画片也不是低幼倾向的文化产品。性格转变过快，密集迎合观众笑点之类的缺陷有不少，但来日可期，可以再打磨。\"}, {\"short_date\": \"2019-07-19\", \"short_star\": \"30\", \"short_title\": \"还行\", \"short_content\": \"全程冷漠脸，我太讨厌熊孩子了，尤其是这么丑破坏力还这么强的。还有给小孩配不屑御姐音让我感到不适。\"}, {\"short_date\": \"2019-07-26\", \"short_star\": \"40\", \"short_title\": \"推荐\", \"short_content\": \"人不过就是半神半魔的造物，这故事按照这个路子衍生。整体非常工整，技术让人赞叹，自《大圣归来》到《哪吒》，这条从中国神话拿改素材的动画之路被证明是最经济实惠的。这里面其实有着另外可以深化的内容，就是几个角色的象征，哪吒像个为民请命的知识分子，但被庸众看作妖怪，他的叛逆不被理解和尊重，龙王是个归顺的反叛者，但被招安并不代表被信任，他的下场故事里讲得很清楚，而敖丙是甩脱出身帽子的唯一机会，而最终，这个年轻人和哪吒那个反叛者合二为一成为一个被大众颔首的理中客。这到底是成熟还是悲哀呢？只不过这个方向肯定不会被明确提点。想想有点悲哀，动画片的形式让这类作品成为了我们电影中最可能表达一些别样内容的容器，但也因为形式，那些表达最终被掩埋在搞笑和特效之中。\"}, {\"short_date\": \"2019-07-17\", \"short_star\": \"20\", \"short_title\": \"较差\", \"short_content\": \"这不叫难看这叫什么？剧情低幼主题无趣想法无聊笑点基本都是八百年前的 唯独制作不错 但一枝独秀有什么用 如果这片是国漫之光 那国漫也算病入膏肓了\"}, {\"short_date\": \"2019-07-17\", \"short_star\": \"30\", \"short_title\": \"还行\", \"short_content\": \"偏低幼向，剧情含量比大圣归来要多，但观感没有超越大圣，顶多比肩白蛇。有些影评人拿它踩大圣，我？？？亮点在于重写了敖丙和哪吒的关系，正邪一体，反宿命论，龙宫和万鳞甲的设定我很喜欢。但为了故事革新，削肉还母削骨还父的经典场面没了，最后的终极大战也没有燃到新境界。人物台词融入一些现代化的笑点，确实更搞笑，但我出戏很多次，奇幻题材的沉浸感很重要。太乙真人从外形到配音都像pdd，哪吒的傲娇御姐音什么鬼。（炒cp可真好卖）神话英雄在不同时代被不同创作者赋予不同的涵义，你以为它是骨，其实它是壳。 朋友说“你不能否认魔童它很当下。” 所以大圣归来不讲大闹天宫，哪吒也不讲闹海自刎。 是时代的反骨逆鳞被拔除了，我们都是龙宫里的老龙。\"}, {\"short_date\": \"2019-07-21\", \"short_star\": \"20\", \"short_title\": \"较差\", \"short_content\": \"国产动画发展了这么多年，似乎是越来越不明白技术它就不是这个行当里最根本的东西，不明白作品里塞再多大而空的感情也无法真正打动人。古往今来反父权反愚孝的动画人物有几个？这么一个难能可贵的形象还给毁了，改得面目全非为什么还要继续叫哪吒？就是叫王小明也完全没问题。至于笑点，永远低俗而不自知，片里翻来覆去地嘲笑结巴、胖子和娘娘腔，有意思吗？做动画的各位是大人了都这样子，还指望我们的动画教出什么样的小孩？\"}, {\"short_date\": \"2019-07-14\", \"short_star\": \"50\", \"short_title\": \"力荐\", \"short_content\": \"神话故事新编，以一种不令人悲伤的方式来讲述悲伤的哪吒童年。丰富多元充满想象力画面；包含幽默、热血、感人和人生观点的剧情；还有安排得当的叙事节奏，结尾处高潮更是一波接一波，让观众又是激动万分，又是感动落泪，实在令人佩服，这就是一部优秀的动画电影。\"}, {\"short_date\": \"2019-07-13\", \"short_star\": \"40\", \"short_title\": \"推荐\", \"short_content\": \"童年时期，最难忘的一个画面就是哪吒自刎！这么多年过去了，又看到了一个看起来丑爆丑爆的哪吒。故事在原作基础上做了颠覆性改编，面子上不必多说，里子中关于父爱的感动，自我认知的成长，世俗偏见的以及反叛意识，都值得称道。还有很多现代化元素的融合也别有趣味！自来水安利，去看就对了…\"}, {\"short_date\": \"2019-07-19\", \"short_star\": \"50\", \"short_title\": \"力荐\", \"short_content\": \"看完就想卧槽！！！太特么好看了！！！这是我观影史上第一次观众自发鼓掌！！！哪吒小爷太值得了！！！跟敖丙CP太好嗑了！！！等上映了我要二刷！！！大家不去电影院真的会后悔死！我错过了开场十分钟，肠子都悔青了！！！\"}, {\"short_date\": \"2019-07-19\", \"short_star\": \"50\", \"short_title\": \"力荐\", \"short_content\": \"暑期档到目前为止最好看的一部。真正打动我的不是哪吒的人设，而是找回了久违的看港片喜剧的快感！\"}, {\"short_date\": \"2019-07-21\", \"short_star\": \"30\", \"short_title\": \"还行\", \"short_content\": \"陈塘关的百姓跪谢哪吒的时候没有意识到，要是没哪吒和敖丙这俩小兔崽子，它陈塘关也万万不会遭此大劫……\"}]');
/*!40000 ALTER TABLE `shorts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-04 15:42:12
