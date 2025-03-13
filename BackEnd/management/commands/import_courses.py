from django.core.management.base import BaseCommand
from BackEnd.models import *

class Command(BaseCommand):
    help = 'Import courses from predefined dictionaries into the database.'

    def handle(self, *args, **options):
        # First set of courses
        classes = [
            {
                "class_name": "COMP 405",
                "title": "Introduction Database Systems",
                "description": "Physical data organization; hierarchical, network and relational models; design theory for databases, normal forms, query optimization; integrity and security. Includes application implementation.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 406",
                "title": "Computer Architecture",
                "description": "Design/simulation of modern computer architecture principles, microprocessor/memory design. Covers pipelining, multicore, caches, hardware-software interface, and prototyping hardware.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 407",
                "title": "Embedded Systems",
                "description": "Hardware/firmware design with sensor integration. Covers embedded processors, circuit design, FPGA boards, communication protocols (RS-232/SPI/I2C). Includes hardware lab.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 415",
                "title": "Emerging Languages",
                "description": "Exploration of niche/emerging programming languages. Covers language idioms, toolchains, abstraction patterns, and programming paradigms. Repeatable up to 6 credits.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 418",
                "title": "Data Mining",
                "description": "Predictive/descriptive methods including classification, clustering, association analysis. Covers text mining, data visualization, and ethical data practices.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 419",
                "title": "Web Information Retrieval",
                "description": "Text-based information systems design. Covers text indexing, retrieval models (vector space/probabilistic), web crawling, recommender systems, and evaluation methods.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 426",
                "title": "2D Game Design",
                "description": "2D game development lifecycle. Focuses on scrolling mechanics, tiled maps, game AI (pathing/goal selection), and art copyright issues.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 430",
                "title": "Computer Networks",
                "description": "Data transmission, multiplexing, switching, transmission media. Covers error/line control, packet switching networks, and network modeling.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 431",
                "title": "Wireless Networks and Security",
                "description": "Wireless protocols/standards (cellular/WLAN/ad hoc). Covers security, radio resource management, mobility control, and TCP adaptations.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 435",
                "title": "Analysis of Algorithms",
                "description": "Algorithm efficiency analysis. Covers data manipulation, graphical analysis, algebraic functions, and NlogN sorting bounds.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 436",
                "title": "Computer Graphics",
                "description": "Graphics hardware/algorithms. Includes affine transformations, clipping, splines, projections, solid modeling, and shading techniques.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 437",
                "title": "Simulation and Game Design",
                "description": "Game development using engines/modeling software. Team-based game implementation with historical context.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 460",
                "title": "Introduction to Robotics",
                "description": "Robot manipulator theory. Covers motion mathematics, programming, control, sensing, and planning.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 461",
                "title": "History of Computing",
                "description": "Evolution of computing technologies. Includes hands-on work with historical systems/emulations.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 462",
                "title": "Distributed Systems",
                "description": "Design of scalable/fault-tolerant systems. Covers RPC, distributed synchronization, replication, consensus algorithms, and MapReduce.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 463",
                "title": "Machine Learning",
                "description": "Algorithms for pattern discovery/prediction. Covers interdisciplinary approaches and real-world applications.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 470",
                "title": "Intro Artificial Intelligence",
                "description": "AI concepts with focus on representation/data structures. Introduces LISP or similar languages.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 485",
                "title": "Honors Capstone Comp Science",
                "description": "Departmental honors project requiring faculty mentorship. Repeatable up to 6 credits.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 490",
                "title": "Senior Design & Development",
                "description": "Capstone team project integrating CS fundamentals. Requires critical analysis of societal impacts.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 498",
                "title": "Internship in Computer Science",
                "description": "Fieldwork in CS with departmental supervision. Minimum 10 hrs/week.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 499",
                "title": "Directed Study Comp Science",
                "description": "Independent project for juniors/seniors. Repeatable up to 6 credits.",
                "credit_hours": 3
            },
            # From 3@.pdf
            {
                "class_name": "COMP 320",
                "title": "Unix/Linux System Admin",
                "description": "Unix/Linux administration: file organization, backups, security, scripting. Includes shell scripting for system tasks.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 334",
                "title": "Algorithmic Art",
                "description": "Computer-generated art using fractals, Perlin noise, L-systems. Culminates in public exhibition.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 335",
                "title": "Web Application Development",
                "description": "Modern web technologies: client/server scripting, databases, security/privacy issues.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 340",
                "title": "Organization of Program Lang",
                "description": "Programming language paradigms and problem-solving approaches. Covers multiple language types.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 345",
                "title": "Compiler Construction",
                "description": "Compiler structure: lexing, parsing, optimization. Students build a sample compiler.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 350",
                "title": "Operating Systems",
                "description": "OS organization for batch/multiprocessing systems. Covers concurrency, memory management, and file systems.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 351",
                "title": "Computer Forensics",
                "description": "Digital forensics on OS platforms. Hands-on evidence acquisition/analysis.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 352",
                "title": "Mobile Device Forensics",
                "description": "iOS/Android forensics: architecture, data extraction, security analysis with Python.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 353",
                "title": "Multimedia Systems Forensics",
                "description": "Media forensics: acquisition, steganography, DRM. Practical application development.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 361",
                "title": "Introduction to Cybersecurity",
                "description": "Cybersecurity fundamentals: networks, cryptography, malware, defense strategies.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 362",
                "title": "Cybersecurity Incident Resp",
                "description": "Incident detection/response: evidence collection, remediation planning.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 363",
                "title": "Applied Cryptography",
                "description": "Cryptographic algorithms: encryption, hashing, signatures. Protocol analysis for real-world applications.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 390",
                "title": "Software Engineering",
                "description": "Full software lifecycle: communication, testing, deployment. Uses modern models/tools.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 397",
                "title": "Topics in Computer Engineering",
                "description": "Special topics in computer engineering. Repeatable for different topics.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 398",
                "title": "Topics: Cyber Digital Forensic",
                "description": "Advanced cybersecurity/forensics topics. Repeatable up to 6 credits.",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 399",
                "title": "Topics in Computer Science",
                "description": "Special topics in CS. Prerequisites vary by topic. Repeatable.",
                "credit_hours": 3
            }
        ]

        # Second set of courses
        classes2 = [
            {
                "class_name": "ENGL 101E",
                "title": "Writing Rhetorically",
                "description": None,
                "credit_hours": 3
            },
            {
                "class_name": "ENGL 102",
                "title": "Write Rhetorically with Sources",
                "description": None,
                "credit_hours": 3
            },
            {
                "class_name": "CRIT 111",
                "title": "Foundations of Logical Reasoning",
                "description": None,
                "credit_hours": 3
            },
            {
                "class_name": "MATH 122",
                "title": "College Algebra",
                "description": None,
                "credit_hours": 3
            },
            {
                "class_name": "MATH 150",
                "title": "Precalculus with Trigonometry",
                "description": "Courses taken for Mathematical Reasoning cannot be reused for Quantitative Reasoning.",
                "credit_hours": 4
            },
            {
                "class_name": "LANG 298",
                "title": "2YSem: Vampires, Taboo Desires",
                "description": None,
                "credit_hours": 3
            },
            {
                "class_name": "AMST 220",
                "title": "Intro to American Studies",
                "description": None,
                "credit_hours": 3
            },
            {
                "class_name": "ANTH 212",
                "title": "Africa through Films",
                "description": None,
                "credit_hours": 3
            },
            {
                "class_name": "COMM 102",
                "title": "Intro to Public Speaking",
                "description": None,
                "credit_hours": 3
            },
            {
                "class_name": "ARTH 104",
                "title": "Surv of Global Art 14C-Present",
                "description": None,
                "credit_hours": 3
            },
            {
                "class_name": "THEA 110",
                "title": "Theatre Appreciation",
                "description": None,
                "credit_hours": 3
            },
            {
                "class_name": "LAPO 151",
                "title": "Intermed Portuguese I",
                "description": None,
                "credit_hours": 3
            },
            {
                "class_name": "PHYS 181",
                "title": "Elements of Physics I",
                "description": "Satisfied by PHYS151 - College Physics I - Massasoit Community College.",
                "credit_hours": 4
            },
            {
                "class_name": "GEOL 194",
                "title": "Environmental Geology",
                "description": None,
                "credit_hours": 3
            },
            {
                "class_name": "POLI 172",
                "title": "Intro to American Government",
                "description": None,
                "credit_hours": 3
            },
            {
                "class_name": "COMP 151",
                "title": "Computer Science I",
                "description": None,
                "credit_hours": 3
            },
            {
                "class_name": "COMP 152",
                "title": "Computer Science II",
                "description": None,
                "credit_hours": 4
            },
            {
                "class_name": "COMP 206",
                "title": "Intro Computer Organization",
                "description": None,
                "credit_hours": 4
            },
            {
                "class_name": "COMP 250",
                "title": "Data Structures and Algorithms",
                "description": None,
                "credit_hours": 3
            },
            {
                "class_name": "COMP 340",
                "title": "Organization of Program Lang",
                "description": "In-progress (2025 SPRING).",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 350",
                "title": "Operating Systems",
                "description": None,
                "credit_hours": 3
            },
            {
                "class_name": "COMP 390",
                "title": "Software Engineering",
                "description": None,
                "credit_hours": 3
            },
            {
                "class_name": "MATH 120",
                "title": "Introduction to Linear Algebra",
                "description": "In-progress (2025 SPRING).",
                "credit_hours": 3
            },
            {
                "class_name": "MATH 130",
                "title": "Discrete Mathematics I",
                "description": None,
                "credit_hours": 3
            },
            {
                "class_name": "MATH 161",
                "title": "Single Variable Calculus I",
                "description": "Satisfied by MATH221 - Calculus I - Massasoit Community College.",
                "credit_hours": 4
            },
            {
                "class_name": "MATH 162",
                "title": "Single Variable Calculus II",
                "description": "Satisfied by MATH222 - Calculus II - Massasoit Community College.",
                "credit_hours": 4
            },
            {
                "class_name": "MATH 200",
                "title": "Statistical Methods I",
                "description": "In-progress (2025 SPRING).",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 335",
                "title": "Web Application Development",
                "description": "In-progress (2025 SPRING).",
                "credit_hours": 3
            },
            {
                "class_name": "COMP 463",
                "title": "Machine Learning",
                "description": "In-progress (2025 SPRING).",
                "credit_hours": 3
            },
            {
                "class_name": "PHYS 182",
                "title": "Elements of Physics II",
                "description": "Satisfied by PHYS152 - College Physics II - Massasoit Community College.",
                "credit_hours": 4
            },
            {
                "class_name": "COMP 143",
                "title": "Intro Comp Sci:Peer Assist",
                "description": "1.0 credit co-requisite for COMP 151 at BSU.",
                "credit_hours": 1
            },
            {
                "class_name": "COMM 103",
                "title": "Introduction to Film",
                "description": None,
                "credit_hours": 3
            },
            {
                "class_name": "DATA 101",
                "title": "Intro Software Data Analytics",
                "description": "In-progress (2025 SPRING).",
                "credit_hours": 3
            },
            {
                "class_name": "ENGL 144",
                "title": "Academic Strategies Colloquium",
                "description": None,
                "credit_hours": 1
            },
            {
                "class_name": "LAPO 100",
                "title": "Portuguese Special Purposes",
                "description": None,
                "credit_hours": 3
            }
        ]

        # Combine both course lists
        all_courses = classes + classes2

        for course in all_courses:
            subject, created = Subject.objects.get_or_create(
                name=course.get("class_name"),
                defaults={
                    "title": course.get("title"),
                    "description": course.get("description"),
                    "credit_hours": course.get("credit_hours")
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created subject: {subject}"))
            else:
                self.stdout.write(self.style.WARNING(f"Subject already exists: {subject}"))

        self.stdout.write(self.style.SUCCESS("Course import complete."))
