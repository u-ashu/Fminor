import Logo from "../common/Logo";

import {
    Plus,
    MessageSquare,
    FileText,
    Library,
    Scale,
    BookOpen,
    Star,
    Settings,
    ChevronRight,
} from "lucide-react";

const menu = [
    {
        icon: MessageSquare,
        title: "Chats",
    },
    {
        icon: FileText,
        title: "My Papers",
    },
    {
        icon: Library,
        title: "Library",
    },
    {
        icon: Scale,
        title: "Compare",
    },
    {
        icon: BookOpen,
        title: "Literature",
    },
    {
        icon: Star,
        title: "Favorites",
    },
    {
        icon: Settings,
        title: "Settings",
    },
];

export default function Sidebar() {
    return (
        <aside
            className="
            hidden
            md:flex
            md:w-64
            lg:w-72
            xl:w-80
            shrink-0
            flex-col
            border-r
            border-white/10
            bg-[#0B1120]
        "
        >
            {/* Logo */}

            <div className="p-6">

                <Logo />

            </div>

            {/* New Chat */}

            <div className="px-6">

                <button
                    className="
                    flex
                    w-full
                    items-center
                    justify-center
                    gap-2
                    rounded-xl
                    bg-violet-600
                    py-3
                    font-medium
                    transition
                    hover:bg-violet-500
                "
                >
                    <Plus size={18} />

                    New Chat

                </button>

            </div>

            {/* Menu */}

            <div className="mt-8 flex-1 space-y-2 px-4">

                {menu.map(({ icon: Icon, title }) => (
                    <button
                        key={title}
                        className="
                        flex
                        w-full
                        items-center
                        justify-between
                        rounded-xl
                        px-4
                        py-3
                        text-slate-300
                        transition
                        hover:bg-white/5
                        hover:text-white
                    "
                    >
                        <div className="flex items-center gap-3">

                            <Icon size={18} />

                            {title}

                        </div>

                        <ChevronRight size={16} />

                    </button>
                ))}

            </div>

            {/* User */}

            <div className="border-t border-white/10 p-5">

                <div className="rounded-xl bg-white/5 p-4">

                    <h3 className="font-semibold">

                        Ashutosh

                    </h3>

                    <p className="text-sm text-slate-400">

                        Free Plan

                    </p>

                </div>

            </div>

        </aside>
    );
}